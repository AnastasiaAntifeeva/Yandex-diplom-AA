
# Анастасия Антифеева, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# Тест: По треку заказа можно получить данные о заказе
def test_get_order_by_track():
    # Создаем заказ и получаем номер трека
    response = sender_stand_request.post_new_order(data.order_body)
    order_track = response.json().get("track")

    # Выполняем запрос на получение заказа по треку
    response = sender_stand_request.get_order(order_track)

    # Проверяем, что код ответа равен 200
    assert response.status_code == 200