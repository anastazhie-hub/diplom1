import sender_stand_request
import data

params = {
    "t": 448618
}

def get_order_info(params):
    current_body = data.order_track.copy()
    current_body["t"] = params
    return current_body

def test_find_order_info():
    data.order_track = get_order_info(params)
    response = sender_stand_request.post_order(data.order_body)
    assert response.status_code == 200