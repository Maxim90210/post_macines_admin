class ParcelTestCase(TestCase):
    def test_parcel_validation(self):
        parcel = Parcel(recipient='')
        with self.assertRaises(ValidationError):
            parcel.full_clean()
