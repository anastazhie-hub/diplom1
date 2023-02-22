import sender_stand_request
import configuration
import data

def test_find_order_info():
    response = sender_stand_request.post_order(data.order_body)
    data.track = {"t": response.json()["track"]}


def get_order_info():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_INFO_PATH,
                        params=data.track)
    assert response.status_code == 200