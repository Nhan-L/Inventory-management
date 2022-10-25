
from StockManage import StockManage

class Login:
    error = None
    def __init__(self, uid, passw):
        self.uid = "admin"
        self.passw = "admin"
        Login.error = "Enter a valid user id and password"

    def authenticate(self):
        if (self.uid == logid and self.passw == logpass):
            print ("Login successful")
            # khởi tạo một đối tượng Quanlyhangtonkho để quản lý hàng tồn kho
            qlst = StockManage()
            while (1==1):
                print("\nCHUONG TRINH QUAN LY HANG TON KHO PYTHON")
                print("*************************MENU**************************")
                print("**  1. Them hang ton kho.                            **")
                print("**  2. Cap nhat thong tin hang ton kho boi IDStock.  **")
                print("**  3. Xoa hang ton kho boi IDStock.                 **")
                print("**  4. Tim kiem hang ton kho theo name.              **")
                print("**  5. Sap xep hang ton kho theo Unit.               **")
                print("**  6. Sap xep hang ton kho theo Name.               **")
                print("**  7. Sap xep hang ton kho theo IDStock.            **")
                print("**  8. Hien thi danh sach hang ton kho.              **")
                print("**  0. Thoat                                         **")
                print("*******************************************************")
                
                key = int(input("Nhap tuy chon: "))
                if (key == 1):
                    print("\n1. Them hang ton kho.")
                    qlst.enter_inventory_information()
                    print("\nThem hang ton kho thanh cong!")
                elif (key == 2):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n2. Cap nhat thong tin hang ton kho boi IDStock.")
                        print("\nNhap IDStock: ")
                        IDStock = input()
                        qlst.updatestock(IDStock)
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 3):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n3. Xoa hang ton kho.")
                        print("\nNhap IDStock: ")
                        IDStock = input()
                        if (qlst.deleteByIDStock(IDStock)):
                            print("\nHang ton kho co IDStock = ", IDStock, " da bi xoa.")
                        else:
                            print("\nHang ton kho co IDStock = ", IDStock ," khong ton tai.")
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 4):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n4. Tim kiem hang ton kho theo ten.")
                        print("\nNhap ten de tim kiem: ")
                        Name = input()
                        searchResult = qlst.findByName(Name)
                        qlst.showStock(searchResult)
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 5):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n5. Sap xep hang ton kho theo Unit.")
                        qlst.sortByUnit()
                        qlst.showStock(qlst.getListStock())
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 6):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n6. Sap xep hang ton kho theo ten.")
                        qlst.sortByName()
                        qlst.showStock(qlst.getListStock())
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 7):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n6. Sap xep hang ton kho theo IDStock.")
                        qlst.sortByIDStock()
                        qlst.showStock(qlst.getListStock())
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 8):
                    if (qlst.quantity_of_inventory() > 0):
                        print("\n7. Hien thi danh sach hang ton kho.")
                        qlst.showStock(qlst.getListStock())
                    else:
                        print("\nDanh sach hang ton kho trong!")
                elif (key == 0):
                    print("\nBan da chon thoat chuong trinh!")
                    break
                else:
                    print("\nKhong co chuc nang nay!")
                    print("\nHay chon chuc nang trong hop menu.")
        else:
            print (Login.error)

log = Login("", "")
logid = input("Enter your user ID: ")
logpass = input("Enter your password: ")

log.authenticate()


