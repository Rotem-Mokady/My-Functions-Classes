#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Excel:
    class pandas:
        def get_excel(self):
            import pandas as pd
            try:
                end = pd.read_excel(str(self) + ".xlsx")
            except:
                end = pd.read_csv(str(self) + ".csv")
            return end

