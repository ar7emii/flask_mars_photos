import requests



class MarsRoversParsing:
    JSON = None
    photo_camera_sequence = []

    def get_data(self, date):
        try:
            temp = date.split(".")
            y = temp[0]
            m = temp[1]
            d = temp[2]
            url = 'http://mars-photos.herokuapp.com/api/v1/rovers/Curiosity/photos?earth_date={}-{}-{}'.format(y, m, d)
            self.JSON = requests.get(url=url).json()
            photos_data = self.JSON['photos'][:15]
            photos_links = []
            camera_type = []
            for i in range(len(photos_data)):
                photos_links.append(photos_data[i]['img_src'])
            for i in range(len(photos_data)):
                camera_type.append(photos_data[i]['camera']['name'])
            if photos_links == []:
                photos_links = 'No photos:('
                camera_type = 'No photos:('
                return photos_links, camera_type
            else:
                photo_camera_sequence = list(zip(photos_links, camera_type))
                self.photo_camera_sequence = photo_camera_sequence
                return photo_camera_sequence

        except IndexError:
            photos_links = 'Input error:('
            camera_type = 'Input error:('
            return photos_links, camera_type

# a = MarsRoversParsing()
# print(a.get_data('2023.1.1'))
