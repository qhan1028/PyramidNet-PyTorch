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
    local('docker build -t {} -f {} {}'.format(image, dockerfile_path, base_path))

@task
def run(context='ailabs', datapath='data'):
    image = osp.join(registries[context], name)
    local('docker run -it --rm -v {}:/app/data {}').format(datapath, image)
    
@task
def push(context='ailabs'):
    if context != 'local':
        image = osp.join(registries[context], name)
        local('docker push {}'.format(image))