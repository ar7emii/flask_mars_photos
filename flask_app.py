from flask import Flask  # Импорт базового FLASK (на основе которого будем делать свое приложение)
from flask import render_template  # Этот метод на основе которого будет генерироваться ответ от сервера
from flask import request  # Это важная переменная содержащая в себе информацию от Клиента
from mars_rovers_parsing import MarsRoversParsing

# # 1. Создать веб-приложение "app" из класса Flask
print("Запуск сайта!")
flag_host = True
app = Flask(__name__)  # Не меняем название этой переменной
# Создали объекты для парсинга
mars_rovers_parsing_class = MarsRoversParsing()


# 2. Основная логика веб-приложения


@app.route("/", methods=['GET', 'POST'])
def index():
    def create_tables(d):
        photos = mars_rovers_parsing_class.get_data("{}".format(d))

        return photos

    if request.method == 'GET':
        table_rover_photos = create_tables('2023.01.01')
        return render_template('index.html', DATE1='2023.01.01', TABLE1=table_rover_photos)
    if request.method == 'POST':
        date_of_photos = request.form["date_of_photos"]
        select_camera = request.form["select_camera_type"]
        table_rover_photos = []

        if select_camera == 'ANY':
            table_rover_photos = create_tables(date_of_photos)
        elif select_camera == 'FHAZ':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'FHAZ':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        elif select_camera == 'ENTRY':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'ENTRY':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        elif select_camera == 'MINITES':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'MINITES':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        elif select_camera == 'NAVCAM':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'NAVCAM':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        elif select_camera == 'PANCAM':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'PANCAM':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        elif select_camera == 'RHAZ':
            table_rover_photos = []
            for i in mars_rovers_parsing_class.photo_camera_sequence:
                if i[1] == 'RHAZ':
                    table_rover_photos.append(i)
                else:
                    pass
            if table_rover_photos == []:
                table_rover_photos = 'No photos were taken on that camera:('
        return render_template('index.html', DATE1=date_of_photos, TABLE1=table_rover_photos)


if __name__ == '__main__':
    app.run()
