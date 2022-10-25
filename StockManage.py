from Stock import Stock
       
import math

class StockManage:
    listStock = []
 
    # Hàm tạo thứ tự tăng dần cho vật tư
    def numerical_order(self):
        maxId = 1
        if (self.quantity_of_inventory() > 0):
            maxId = self.listStock[0]._id
            for st in self.listStock:
                if (maxId < st._id):
                    maxId = st._id
            maxId = maxId + 1
        return maxId
 
    def quantity_of_inventory(self):
        return self.listStock.__len__()
 
    def enter_inventory_information(self):
        # Khởi tạo một hang ton kho moi
        StId = self.numerical_order()
        Input_day = input("Enter Inventory Import Date_Input_day: ")
        IDStock = input("Enter inventory code_IDStock: ")
        Name = input("Enter an inventory name_Name: ")
        Unit = input("Enter inventory calculation units_Unit: ")
        Amount = float(input("Enter inventory quantity_Amount: "))
        Unit_price = float(input("Enter inventory unit price_Unit_price: "))
        Staff_input = input("Enter the input Staff's name_Staff_input: ")
        st = Stock(StId, Input_day, IDStock, Name, Unit, Amount, Unit_price, Staff_input)
        self.Total_amount(st)
        self.listStock.append(st)
 
    def updatestock(self, IDStock):
        # Tìm kiếm hàng tồn kho trong danh sách listStock bằng IDStock
        st:Stock = self.findByIDStock(IDStock)
        # Nếu hàng tồn kho đã tồn tại thì cập nhập thông tin hàng tồn kho
        if (st != None):
            # Cập nhập thông tin hàng tồn kho
            Input_day = input("Enter Inventory Import Date_Input_day: ")
            IDStock = input("Enter inventory code_IDStock: ")
            Name = input("Enter an inventory name_Name: ")
            Unit = input("Enter inventory calculation units_Unit: ")
            Amount = float(input("Enter inventory quantity_Amount: "))
            Unit_price = float(input("Enter inventory unit price_Unit_price: "))
            Staff_input = input("Enter the input Staff's name_Staff_input: ")
            # cập nhật thông tin hàng tồn kho
            st._Input_day = Input_day
            st._IDStock = IDStock
            st._Name = Name
            st._Unit = Unit
            st._Amount = Amount
            st._Unit_price = Unit_price
            st._Staff_input = Staff_input
            self.Total_amount(st)
            self.listStock.append(st)
        else:
            print("Hang ton kho da co ID = {} khong ton tai.".format(IDStock))
 
    # Hàm sắp xếp danh sach hàng tồn kho theo số đơn vị tính tăng dần
    # lambda hàm định danh
    def sortByUnit(self):
        self.listStock.sort(key=lambda x: x._Unit, reverse=False)
 
    #Hàm sắp xếp danh sach hàng tồn kho theo tên tăng dần
    def sortByName(self):
        self.listStock.sort(key=lambda x: x._Name, reverse=False)
 
    # Hàm sắp xếp danh sach sinh vien theo IDStock tăng dần
    def sortByIDStock(self):
        self.listStock.sort(key=lambda x: x._IDStock, reverse=False)
 
    # Hàm tìm kiếm hàng tồn kho theo IDStock
    # Trả về một hàng tồn kho
    def findByIDStock(self, IDStock):
        searchResult = None
        if (self.quantity_of_inventory() > 0):
            for st in self.listStock:
                if (st._IDStock == IDStock):
                    searchResult = st
        return searchResult
 
    # Hàm tìm kiếm hàng tồn kho theo tên
    # Trả về một danh sách hàng tồn kho
    def findByName(self, keyword):
        listSt = []
        if (self.quantity_of_inventory() > 0):
            for st in self.listStock:
                if (keyword.upper() in st._Name.upper()):
                    listSt.append(st)
        return listSt
 
    # Hàm xóa hàng tồn kho theo IDStock
    def deleteByIDStock(self, IDStock):
        isDeleted = False
        # tìm kiếm hàng tồn kho theo IDStock
        st = self.findByIDStock(IDStock)
        if (st != None):
            self.listStock.remove(st)
            isDeleted = True
        return isDeleted
 
    # Hàm tính tổng tiền hàng tồn kho
    def Total_amount(self, st:Stock):
        Total_amount = st._Unit_price * st._Amount
        # làm tròn tổng tiền với 2 chữ số thập phân
        st._Total_amount = math.ceil(Total_amount * 100) / 100
 
    
    # Hàm hiển thị danh sách hàng tồn kho ra màn hình console
    def showStock(self, listSt):
        # hien thi tieu de cot
        print("{:<6} {:<12} {:<10} {:<10}{:<10} {:<12} {:<14} {:<14} {:<14}"
              .format("Id", "Input_day", "IDStock", "Name", "Unit", "Amount", "Unit_price", 
              "Staff_input", "Total_amount"))
            
        # hien thi danh sach hang ton kho
        if (listSt.__len__() > 0):
            for st in listSt:
                print("{:<6} {:<12} {:<10} {:<10}{:<10} {:<12} {:<14} {:<14} {:<14}"
                      .format(st._id, st._Input_day, st._IDStock, st._Name, st._Unit, 
                      st._Amount, st._Unit_price, st._Staff_input, st._Total_amount))
        print("\n")
 
    # Hàm trả về danh sách hàng tồn kho hiện tại
    def getListStock(self):
        return self.listStock




