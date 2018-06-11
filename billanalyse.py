# coding: utf-8
import csv
import chardet

def Analysing(filename,total_line_number):
    with open(filename) as f:
        reader = csv.reader(f)
        property_str=[]
        line_cnt=0
        for line_list in reader:
            line_cnt = line_cnt +1
            if line_cnt == 5:
                property_list = line_list
                break

        line_cnt=0
        static_info={}

        for line_list in reader:
            line_cnt = line_cnt +1
            # print "line_cnt =",line_cnt
            if line_cnt > total_line_number:
                break
            if line_cnt > 5:
                if "支出" in line_list[10] and "交易成功" in line_list[11]:
                    if line_list[7] in static_info:
                        static_info[line_list[7]] = static_info[line_list[7]]+float(line_list[9])
                        # print "static_info[",line_list[7],"] =",static_info[line_list[7]]
                    else:
                        static_info[line_list[7]] = float(line_list[9])

        # for key in static_info:
        #     print key,"= ",static_info[key]
        import operator
        infos = sorted(static_info.items(), key=operator.itemgetter(1))
        total_money =0
        for info in infos:
            print info[0]," ",info[1]
            total_money = total_money+ info[1]

        print "total_money = ",total_money

def WechatBill(file_name):
    total_cost_money=0
    line_cnt = 0
    static_info={}
    with  open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_cnt += 1
            if line_cnt%5==1:
                name = line.split('\n')[0]
            if line_cnt%5==3:
                if '-' ==line.split(' ')[0]:
                    data = -float(line.split(' ')[1])
                # elif '+' ==line.split(' ')[0]:
                #     data = float(line.split(' ')[1])
                # print name,"=",data
                if name in static_info:
                    static_info[name] += data
                else:
                    static_info[name] = data
    import operator
    infos = sorted(static_info.items(), key=operator.itemgetter(1))
    for info in infos:
        print info[0], " ", info[1]
        total_cost_money = total_cost_money + info[1]

    print "total_cost_money = ", total_cost_money

    # print "total_cost_money of wechat=",total_cost_money



if __name__ == '__main__':
    # filename = 'wyq.csv'
    # total_line_number = 474
    # Analysing(filename, total_line_number)

    file_wechat ="wechat_bill.txt"
    WechatBill(file_wechat)

    # filename = 'ckl.csv'
    # total_line_number =957
    # Analysing(filename, total_line_number)