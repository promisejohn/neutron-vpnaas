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

import unittest


def _discover(loader, path, pattern):
    return loader.discover(path, pattern=pattern, top_level_dir=".")


def load_tests(_, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(tests)

    loader = unittest.loader.TestLoader()
    suite.addTests(_discover(loader,
                             "./neutron_vpnaas/tests/functional/openswan",
                             pattern))
    suite.addTests(_discover(loader,
                             "./neutron_vpnaas/tests/functional/common",
                             pattern))
    return suite
