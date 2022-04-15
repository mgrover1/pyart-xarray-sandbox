import pyart
import xarray as xr
import xcollection as xc

from xradar import create_dataset_from_sweep, convert_to_xradar

test_radar = pyart.io.read(pyart.testing.get_test_data('110635.mdv'))
                   
def test_create_dataset_from_sweep(test_radar=test_radar):
    xradar_single_sweep = create_dataset_from_sweep(test_radar)
    assert isinstance(xradar_single_sweep, xr.Dataset)

def test_convert_to_xradar(test_radar=test_radar):
    xradar_dataset = convert_to_xradar(test_radar)
    assert isinstance(xradar_dataset, xc.Collection)