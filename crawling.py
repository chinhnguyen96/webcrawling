#!/usr/bin/env python
# coding: utf-8

# # Installation requirements
# 1. pip install pandas
# 2. pip install lxml 
# 3. pip install BeautifulSoup4

# In[3]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


#Đếm số lượng bảng trên trang web
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_phim_%C4%91i%E1%BB%87n_%E1%BA%A3nh_c%E1%BB%A7a_V%C5%A9_tr%E1%BB%A5_%C4%90i%E1%BB%87n_%E1%BA%A3nh_Marvel'

wikitables = read_html(page, index_col=0, attrs={"class":"wikitable"})

print ("Extracted {num} wikitables".format(num=len(wikitables)))


# ## Giai đoạn 1
# 1. Tổng hợp các phim
# 2. Nội dung tóm tắt từng phim

# In[5]:


#Tổng hợp phim
wikitables[0].head(6)


# In[109]:


#Người sắt
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_S%E1%BA%AFt_(phim_2008)'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[110]:


#Người khổng lồ xanh phi thường
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_kh%E1%BB%95ng_l%E1%BB%93_xanh_phi_th%C6%B0%E1%BB%9Dng'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[111]:


#Người sắt 2
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_S%E1%BA%AFt_2'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[112]:


#Thor
page = 'https://vi.wikipedia.org/wiki/Thor_(phim)'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[113]:


#Captain America: Kẻ báo thù đầu tiên
page = 'https://vi.wikipedia.org/wiki/Captain_America:_K%E1%BA%BB_b%C3%A1o_th%C3%B9_%C4%91%E1%BA%A7u_ti%C3%AAn'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[114]:


#Biệt đội siêu anh hùng
page = 'https://vi.wikipedia.org/wiki/Bi%E1%BB%87t_%C4%91%E1%BB%99i_si%C3%AAu_anh_h%C3%B9ng'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# ## Giai đoạn 2
# 1. Tổng hợp các phim
# 2. Nội dung tóm tắt từng phim
# 

# In[116]:


#Tổng hợp phim
wikitables[1].head()


# In[117]:


#Người sắt 3
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_S%E1%BA%AFt_3'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[118]:


#Thor 2: Thế giới Bóng tối
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Thor_2:_Th%E1%BA%BF_gi%E1%BB%9Bi_B%C3%B3ng_t%E1%BB%91i'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[119]:


#Captain America 2: Chiến binh mùa đông
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Captain_America_2:_Chi%E1%BA%BFn_binh_m%C3%B9a_%C4%91%C3%B4ng'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[120]:


#Vệ binh dải Ngân Hà
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/V%E1%BB%87_binh_d%E1%BA%A3i_Ng%C3%A2n_H%C3%A0_(phim)'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[124]:


#Avengers: Đế chế Ultron
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Avengers:_%C4%90%E1%BA%BF_ch%E1%BA%BF_Ultron'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[125]:


#Người Kiến (phim)
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_Ki%E1%BA%BFn_(phim)'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# ## Giai đoạn 3
# 1. Tổng hợp các phim
# 2. Nội dung tóm tắt từng phim

# In[147]:


#Tổng hợp phim
wikitables[2].head(20)


# In[126]:


#Captain America: Nội chiến siêu anh hùng
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Captain_America:_N%E1%BB%99i_chi%E1%BA%BFn_si%C3%AAu_anh_h%C3%B9ng'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[127]:


#Doctor Strange: Phù thủy tối thượng
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Doctor_Strange:_Ph%C3%B9_th%E1%BB%A7y_t%E1%BB%91i_th%C6%B0%E1%BB%A3ng'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[128]:


#Vệ binh dải Ngân Hà 2
from pandas.io.html import read_html
page = 'https://vi.m.wikipedia.org/wiki/V%E1%BB%87_binh_d%E1%BA%A3i_Ng%C3%A2n_H%C3%A0_2'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[129]:


#Người Nhện: Trở về nhà
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_Nh%E1%BB%87n:_Tr%E1%BB%9F_v%E1%BB%81_nh%C3%A0'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[130]:


#Thor: Tận thế Ragnarok
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Thor:_T%E1%BA%ADn_th%E1%BA%BF_Ragnarok'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[131]:


#Black Panther: Chiến binh Báo Đen
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Black_Panther:_Chi%E1%BA%BFn_binh_B%C3%A1o_%C4%90en'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[132]:


#Avengers: Cuộc chiến vô cực
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Avengers:_Cu%E1%BB%99c_chi%E1%BA%BFn_v%C3%B4_c%E1%BB%B1c'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[133]:


#Người Kiến và Chiến binh Ong
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_Ki%E1%BA%BFn_v%C3%A0_Chi%E1%BA%BFn_binh_Ong'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[134]:


#Đại úy Marvel
from pandas.io.html import read_html
page = 'https://vi.m.wikipedia.org/wiki/%C4%90%E1%BA%A1i_u%C3%BD_Marvel_(phim)'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[135]:


#Avengers: Hồi kết
from pandas.io.html import read_html
page = 'https://vi.m.wikipedia.org/wiki/Avengers:_H%E1%BB%93i_k%E1%BA%BFt'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# In[136]:


#Người Nhện xa nhà
from pandas.io.html import read_html
page = 'https://vi.wikipedia.org/wiki/Ng%C6%B0%E1%BB%9Di_Nh%E1%BB%87n_xa_nh%C3%A0'
infoboxes = read_html(page, index_col=0, attrs={"class":"infobox"})

print ("Extracted {num} infoboxes".format(num=len(infoboxes)))
infoboxes[0]


# ## Giai đoạn 4
# 1. Tổng hợp các phim
# 2. Nội dung tóm tắt từng phim

# In[146]:


#Tổng hợp phim
wikitables[3].head(12)


# ## Doanh thu các phim qua từng giai đoạn

# In[148]:


wikitables[4].head(24)

