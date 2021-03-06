# Copyright 2013, Nachi Ueno, NTT I3, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from neutron.agent.l3 import agent as l3_agent
from neutron.agent import l3_agent as entry
from oslo_config import cfg

from neutron_vpnaas.services.vpn import vpn_service

vpn_agent_opts = [
    cfg.MultiStrOpt(
        'vpn_device_driver',
        default=['neutron_vpnaas.services.vpn.device_drivers.'
                 'ipsec.OpenSwanDriver'],
        help=_("The vpn device drivers Neutron will use")),
]
cfg.CONF.register_opts(vpn_agent_opts, 'vpnagent')


class VPNAgent(l3_agent.L3NATAgentWithStateReport):
    """VPNAgent class which can handle vpn service drivers."""
    def __init__(self, host, conf=None):
        super(VPNAgent, self).__init__(host=host, conf=conf)
        self.service = vpn_service.VPNService(self)
        self.device_drivers = self.service.load_device_drivers(host)


def main():
    entry.main(manager='neutron_vpnaas.services.vpn.agent.VPNAgent')
