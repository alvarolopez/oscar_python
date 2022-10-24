# Copyright (C) GRyCAP - I3M - UPV

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 

from oscar_python.cluster import Cluster
import oscar_python._utils as utils

_LOGS_PATH = "/system/logs"
_GET = "get"
_DELETE = "delete"

#TODO test
class Logs:
    def __init__(self, cluster: Cluster) -> None:
        self.cluster = cluster 
    
    def get_job_logs(self, svc, job):
        return utils.make_request(self.cluster, _LOGS_PATH+"/"+svc+"/"+job, _GET)

    def list_jobs(self, svc):
        return utils.make_request(self.cluster, _LOGS_PATH+"/"+svc, _GET)

    def remove_job(self, svc, job):
        return utils.make_request(self.cluster, _LOGS_PATH+"/"+svc+"/"+job, _DELETE)

    def remove_all_jobs(self, svc):
        return utils.make_request(self.cluster, _LOGS_PATH+"/"+svc, _DELETE)