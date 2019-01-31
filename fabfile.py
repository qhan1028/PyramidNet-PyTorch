#
#   Pyramid Net PyTorch Fabfile
#   Written by Liang-Han, 2019.1.31
#

from fabric.api import task, local, hide
import os.path as osp

base_path = osp.realpath(osp.dirname(__file__))

registries = {
    'local': "",
    'ailabs': "registry.corp.ailabs.tw/qhan/crowd-sourcing/",
    'nchc': "hc1.corp.ailabs.tw:6000/"
}
name = 'pyramidnet'
dockerfile_path = osp.join(base_path, 'docker', 'Dockerfile')

def use_context(context):
    local("kubectl config use-context %s" % context)

    
@task
def build(context='ailabs'):
    image = osp.join(registries[context], name)
    local('nvidia-docker build -t {} -f {} {}'.format(image, dockerfile_path, base_path))


# need to specify shared memory size, see the issue: https://github.com/pytorch/pytorch/issues/2244#issuecomment-318864552
@task
def run(context='ailabs', datapath='data'):
    image = osp.join(registries[context], name)
    display_name = '{}-{}'.format(name, context)
    local('nvidia-docker run --rm -d --shm-size 8G --name {} -v {}:/app/data {}'.format(display_name, datapath, image))


@task
def tty(context='ailabs'):
    display_name = '{}-{}'.format(name, context)
    local('docker exec -it {} bash'.format(display_name))

    
@task
def kill(context='ailabs'):
    display_name = '{}-{}'.format(name, context)
    local('docker kill {}'.format(display_name))
    
    
@task
def push(context='ailabs'):
    if context != 'local':
        image = osp.join(registries[context], name)
        local('docker push {}'.format(image))
