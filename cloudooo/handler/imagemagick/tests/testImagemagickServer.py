##############################################################################
#
# Copyright (c) 2009-2011 Nexedi SA and Contributors. All Rights Reserved.
#                    Gabriel M. Monnerat <gabriel@tiolive.com>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
from os.path import join
from cloudooo.tests.cloudoooTestCase import TestCase, make_suite


class TestServer(TestCase):
  """Test XmlRpc Server. Needs cloudooo server started"""

  def ConversionScenarioList(self):
    return [
            (join('data', 'test.png'), "png", "jpg", "image/jpeg"),
            ]

  def testConvertPNGtoJPG(self):
    """Converts png to jpg"""
    self.runConversionList(self.ConversionScenarioList())

  def FaultConversionScenarioList(self):
    return [
            # Test to verify if server fail when a empty string is sent
            ('', '', ''),
            # Try convert one video for a invalid format
            (open(join('data', 'test.png')).read(), 'png', 'xyz'),
            # Try convert one video to format not possible
            (open(join('data', 'test.png')).read(), 'png', '8bim'),
            ]

  def testFaultConversion(self):
    """Test fail convertion of Invalid image files"""

  def GetMetadataScenarioList(self):
    return [
            (join('data', 'test.png'), "png", dict(Compression='Zip')),
            ]

  def testGetMetadataFromPNG(self):
    """test if metadata are extracted correctly from png image file"""
    self.runGetMetadataList(self.GetMetadataScenarioList())

  def FaultGetMetadataScenarioList(self):
    return [
            # Test to verify if server fail when a empty string is sent
            ('', ''),
            ]

  def testFaultGetMetadata(self):
    """Test getMetadata from invalid image file"""
    self.runFaultGetMetadataList(self.FaultGetMetadataScenarioList())


def test_suite():
  return make_suite(TestServer)
