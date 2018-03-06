
# coding: utf-8

# In[1]:


def save_file(wanganshi, ouyangxiu, xinqiji, count):
    file_name_wanganshi = 'wanganshi_' + str(count) +'.txt'
    file_name_ouyangxiu = 'ouyangxiu_' + str(count) +'.txt'
    file_name_xinqiji = 'xinqiji_' + str(count) +'.txt'
    
    wanganshi_file = open(file_name_wanganshi, 'w')
    ouyangxiu_file = open(file_name_ouyangxiu, 'w')
    xinqiji_file = open(file_name_xinqiji, 'w')
    
    wanganshi_file.writelines(wanganshi)
    ouyangxiu_file.writelines(ouyangxiu)
    xinqiji_file.writelines(xinqiji)
    
    wanganshi_file.close()
    ouyangxiu_file.close()
    xinqiji_file.close()

f = open('文件练习.txt')

wanganshi = []
ouyangxiu = []
xinqiji = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        (role,line_spoken) = each_line.split(':', 1)
        if role == '王安石':
            wanganshi.append(line_spoken)
        if role == '欧阳修':
            ouyangxiu.append(line_spoken)
        if role == '辛弃疾':
            xinqiji.append(line_spoken)
    else:
        save_file(wanganshi, ouyangxiu, xinqiji, count)

        wanganshi = []
        ouyangxiu = []
        xinqiji = []
        count += 1
        
save_file(wanganshi, ouyangxiu, xinqiji, count)

f.close()

