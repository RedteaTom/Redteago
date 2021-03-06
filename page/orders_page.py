from page.base_page import BasePage

#全部订单页面
class OrdersPage(BasePage):
    def open_orders(self):
        return self.step('../steps/orders_page.yaml', 'open_orders')

    def close_orders(self):
        return self.step('../steps/orders_page.yaml', 'close_orders')