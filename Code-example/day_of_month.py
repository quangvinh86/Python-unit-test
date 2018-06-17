

def get_day_of_month(month):
    assert (month in range(1, 12)), "Tháng không tồn tại"
    month_list = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October",
                  "November", "December"]
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = (month_list[month - 1], day_list[month - 1])
    return result

if __name__ == "__main__":
    print(get_day_of_month(13))
