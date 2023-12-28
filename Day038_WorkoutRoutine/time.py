from datetime import datetime

today = datetime.now()
ok={
    "name":"Joeysh"
}


print(ok["age"])
actual_date = today.strftime(f"%Y/%m/%d")

actual_time = today.strftime(f"%X")
print(actual_time)