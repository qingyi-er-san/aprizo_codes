import pandas as pd

src_path = 'aprizo_data.xlsx'
df_data = pd.read_excel(src_path)
df_shopify = pd.read_excel('aprizo_shopify.xlsx')

def data_avec_couleur_taille(i):
    '''
     这个函数使用的前提是判断df_data中 Option1的值为 Couleur的时候，
     Args: 
        i ,int,一行数据的index
    '''
    result = []
    if i == 0:
        tailles = df_data.loc[i,'Tailles']
        if not isinstance(tailles,float):
            #这种情况就是产品有多个tailles，需要创造和tailles数量一致的data数据
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]                  
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
                # 这种情况 taille 是 36 37 38 39 40 41这样的
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':df_data.loc[i,'Couleur'],
                    'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    'Option2 Value':int(l_taille_int[0]),
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + l_taille_int[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for taille in l_taille_int[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':df_data.loc[i,'Couleur'],
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    'Option2 Value':int(taille),
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + taille,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                        result.append(new_data1)
            else:
                # 这种情况 taille就是 s ,m , l d
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':df_data.loc[i,'Couleur'],
                    'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    'Option2 Value':list_taille[0],
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + list_taille[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for taille in list_taille[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':df_data.loc[i,'Couleur'],
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    'Option2 Value':taille,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + taille,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                        result.append(new_data1)        
        else:
            # 这种情况就是 产品没有taille这个选项
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
            'Title':df_data.loc[i,'H1(Title)'] ,
            'Body (HTML)':df_data.loc[i,'Description (Body)'],
            'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
            'Product Category':'',
            'Tags':df_data.loc[i,'Tags (tags_type)'],
            'Published':'FAUX',
            'Type':df_data.loc[i,'Tags (tags_type)'],
            'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
            'Option1 Value':df_data.loc[i,'Couleur'],
            #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
            #'Option2 Value':,
            'Option3 Name':None,
            'Option3 Value':None,
            'Variant SKU':df_data.loc[i,'SKU variant'],
            'Variant Grams':df_data.loc[i,'Poids du produit'],
            'Variant Inventory Tracker':'shopify',
            'Variant Inventory Qty':3,
            'Variant Inventory Policy':'deny',
            'Variant Fulfillment Service':'manual',
            'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
            'Variant Compare At Price':None,
            'Variant Requires Shipping':'VRAI',
            'Variant Taxable':'VRAI',
            'Gift Card':'FAUX',
            'Variant Weight Unit':'g',
            'Status':'draft'
            }
            result.append(new_data)
    #判断当前产品是否为 variance，
    elif df_data.loc[i,'SKU principal'] != df_data.loc[i-1,'SKU principal']:
        tailles = df_data.loc[i,'Tailles']
        if not isinstance(tailles,float):
            #这种情况就是产品有多个tailles，需要创造和tailles数量一致的data数据
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
                #taille 为36 37 38        
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                            'Title':df_data.loc[i,'H1(Title)'] ,
                            'Body (HTML)':df_data.loc[i,'Description (Body)'],
                            'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                            'Product Category':'',
                            'Tags':df_data.loc[i,'Tags (tags_type)'],
                            'Published':'FAUX',
                            'Type':df_data.loc[i,'Tags (tags_type)'],
                            'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                            'Option1 Value':df_data.loc[i,'Couleur'],
                            'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                            'Option2 Value':int(l_taille_int[0]),
                            'Option3 Name':None,
                            'Option3 Value':None,
                            'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + l_taille_int[0],
                            'Variant Grams':df_data.loc[i,'Poids du produit'],
                            'Variant Inventory Tracker':'shopify',
                            'Variant Inventory Qty':3,
                            'Variant Inventory Policy':'deny',
                            'Variant Fulfillment Service':'manual',
                            'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                            'Variant Compare At Price':None,
                            'Variant Requires Shipping':'VRAI',
                            'Variant Taxable':'VRAI',
                            'Gift Card':'FAUX',
                            'Variant Weight Unit':'g',
                            'Status':'draft'
                }
                result.append(new_data)
                if len(l_taille_int) > 1:
                    for t in l_taille_int[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':df_data.loc[i,'Couleur'],
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    'Option2 Value':int(t),
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + t,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                        result.append(new_data1)
            else:
                #这种情况就是 taille为 s m l        
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                            'Title':df_data.loc[i,'H1(Title)'] ,
                            'Body (HTML)':df_data.loc[i,'Description (Body)'],
                            'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                            'Product Category':'',
                            'Tags':df_data.loc[i,'Tags (tags_type)'],
                            'Published':'FAUX',
                            'Type':df_data.loc[i,'Tags (tags_type)'],
                            'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                            'Option1 Value':df_data.loc[i,'Couleur'],
                            'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                            'Option2 Value':list_taille[0],
                            'Option3 Name':None,
                            'Option3 Value':None,
                            'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + list_taille[0],
                            'Variant Grams':df_data.loc[i,'Poids du produit'],
                            'Variant Inventory Tracker':'shopify',
                            'Variant Inventory Qty':3,
                            'Variant Inventory Policy':'deny',
                            'Variant Fulfillment Service':'manual',
                            'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                            'Variant Compare At Price':None,
                            'Variant Requires Shipping':'VRAI',
                            'Variant Taxable':'VRAI',
                            'Gift Card':'FAUX',
                            'Variant Weight Unit':'g',
                            'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for t in list_taille[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':df_data.loc[i,'Couleur'],
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    'Option2 Value':t,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + t,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                        result.append(new_data1)
        else:
            # 这种情况就是 产品没有taille这个选项
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                'Title':df_data.loc[i,'H1(Title)'] ,
                'Body (HTML)':df_data.loc[i,'Description (Body)'],
                'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                'Product Category':'',
                'Tags':df_data.loc[i,'Tags (tags_type)'],
                'Published':'FAUX',
                'Type':df_data.loc[i,'Tags (tags_type)'],
                'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                'Option1 Value':df_data.loc[i,'Couleur'],
                #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                #'Option2 Value':,
                'Option3 Name':None,
                'Option3 Value':None,
                'Variant SKU':df_data.loc[i,'SKU variant'],
                'Variant Grams':df_data.loc[i,'Poids du produit'],
                'Variant Inventory Tracker':'shopify',
                'Variant Inventory Qty':3,
                'Variant Inventory Policy':'deny',
                'Variant Fulfillment Service':'manual',
                'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                'Variant Compare At Price':None,
                'Variant Requires Shipping':'VRAI',
                'Variant Taxable':'VRAI',
                'Gift Card':'FAUX',
                'Variant Weight Unit':'g',
                'Status':'draft'
            }
            result.append(new_data)
    # 当前产品为 variance时
    else:
        tailles = df_data.loc[i,'Tailles']
        if not isinstance(tailles,float):
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
                for t in l_taille_int:
                    new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    #'Title':df_data.loc[i,'H1(Title)'] ,
                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    #'Product Category':'',
                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':df_data.loc[i,'Couleur'],
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    'Option2 Value':int(t),
                    #'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + t,
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    #'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    #'Status':'draft'
                    }
                    result.append(new_data)
            else:
                for t in list_taille:
                    new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    #'Title':df_data.loc[i,'H1(Title)'] ,
                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    #'Product Category':'',
                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':df_data.loc[i,'Couleur'],
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    'Option2 Value':t,
                    #'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + t,
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    #'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    #'Status':'draft'
                    }
                    result.append(new_data)
        else:
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                #'Title':df_data.loc[i,'H1(Title)'] ,
                #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                #'Product Category':'',
                #'Tags':df_data.loc[i,'Tags (tags_type)'],
                #'Type':df_data.loc[i,'Tags (tags_type)'],
                #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                'Option1 Value':df_data.loc[i,'Couleur'],
                #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                #'Option2 Value':t,
                #'Option3 Name':None,
                'Option3 Value':None,
                'Variant SKU':df_data.loc[i,'SKU variant'],
                'Variant Grams':df_data.loc[i,'Poids du produit'],
                'Variant Inventory Tracker':'shopify',
                'Variant Inventory Qty':3,
                'Variant Inventory Policy':'deny',
                'Variant Fulfillment Service':'manual',
                'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                'Variant Compare At Price':None,
                'Variant Requires Shipping':'VRAI',
                'Variant Taxable':'VRAI',
                #'Gift Card':'FAUX',
                'Variant Weight Unit':'g',
                #'Status':'draft'
            }
            result.append(new_data)
    return result
def data_avec_taille(i):
    '''
        这个函数使用的前提时判断Option1 == 'Taille'的时候
        Args: 
            i ,int,一行数据的index
    '''
    result = []
    
    if i == 0 :
        tailles = df_data.loc[i,'Tailles']
        # 存在taille
        if not isinstance(tailles,float):
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
                #taille 为36 37 38 
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':int(l_taille_int[0]),
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    #'Option2 Value':36,
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + l_taille_int[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for taille in l_taille_int[1:]:
                            new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':int(taille),
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    #'Option2 Value':taille,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + taille,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                            result.append(new_data1)
            else:
                # taillle 为s m l         
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':list_taille[0],
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    #'Option2 Value':36,
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + list_taille[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for taille in list_taille[1:]:
                            new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':taille,
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    #'Option2 Value':taille,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + taille,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                                    }
                            result.append(new_data1)
        # 没有taille
        else:
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                'Title':df_data.loc[i,'H1(Title)'] ,
                'Body (HTML)':df_data.loc[i,'Description (Body)'],
                'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                'Product Category':'',
                'Tags':df_data.loc[i,'Tags (tags_type)'],
                'Published':'FAUX',
                'Type':df_data.loc[i,'Tags (tags_type)'],
                'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                #'Option1 Value':list_taille[0],
                #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                #'Option2 Value':36,
                'Option3 Name':None,
                'Option3 Value':None,
                'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + list_taille[0],
                'Variant Grams':df_data.loc[i,'Poids du produit'],
                'Variant Inventory Tracker':'shopify',
                'Variant Inventory Qty':3,
                'Variant Inventory Policy':'deny',
                'Variant Fulfillment Service':'manual',
                'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                'Variant Compare At Price':None,
                'Variant Requires Shipping':'VRAI',
                'Variant Taxable':'VRAI',
                'Gift Card':'FAUX',
                'Variant Weight Unit':'g',
                'Status':'draft'
            }
            result.append(new_data) 
    #判断当前产品是否为 variance，
    # 产品部位不为variance的情况
    elif df_data.loc[i,'SKU principal'] != df_data.loc[i-1,'SKU principal']:
        tailles = df_data.loc[i,'Tailles']
        if not isinstance(tailles,float):
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
            #taille 为36 37 38 
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':int(l_taille_int[0]),
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    #'Option2 Value':36,
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + l_taille_int[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for l in l_taille_int[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':int(l),
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    #'Option2 Value':37,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + l,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                        }
                        result.append(new_data1)

            else:
            #taille 为 s m l
                new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    'Title':df_data.loc[i,'H1(Title)'] ,
                    'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    'Product Category':'',
                    'Tags':df_data.loc[i,'Tags (tags_type)'],
                    'Published':'FAUX',
                    'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    'Option1 Value':list_taille[0],
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    #'Option2 Value':36,
                    'Option3 Name':None,
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'] + '-' + list_taille[0],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                    'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    'Status':'draft'
                }
                result.append(new_data)
                if len(list_taille) > 1:
                    for l in list_taille[1:]:
                        new_data1 = {'Handle': df_data.loc[i,'URL(handle)'],
                                    #'Title':df_data.loc[i,'H1(Title)'] ,
                                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                                    #'Product Category':'',
                                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                                    #'Published':'FAUX',
                                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                                    #'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                                    'Option1 Value':l,
                                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                                    #'Option2 Value':37,
                                    'Option3 Name':None,
                                    'Option3 Value':None,
                                    'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + l,
                                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                                    'Variant Inventory Tracker':'shopify',
                                    'Variant Inventory Qty':3,
                                    'Variant Inventory Policy':'deny',
                                    'Variant Fulfillment Service':'manual',
                                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                                    'Variant Compare At Price':None,
                                    'Variant Requires Shipping':'VRAI',
                                    'Variant Taxable':'VRAI',
                                    #'Gift Card':'FAUX',
                                    'Variant Weight Unit':'g',
                                    #'Status':'draft'
                        }
                        result.append(new_data1)
        # 不存在taille
        else:
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                'Title':df_data.loc[i,'H1(Title)'] ,
                'Body (HTML)':df_data.loc[i,'Description (Body)'],
                'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                'Product Category':'',
                'Tags':df_data.loc[i,'Tags (tags_type)'],
                'Published':'FAUX',
                'Type':df_data.loc[i,'Tags (tags_type)'],
                'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                #'Option1 Value':list_taille[0],
                #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                #'Option2 Value':36,
                'Option3 Name':None,
                'Option3 Value':None,
                'Variant SKU':df_data.loc[i,'SKU variant'] ,
                'Variant Grams':df_data.loc[i,'Poids du produit'],
                'Variant Inventory Tracker':'shopify',
                'Variant Inventory Qty':3,
                'Variant Inventory Policy':'deny',
                'Variant Fulfillment Service':'manual',
                'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                'Variant Compare At Price':None,
                'Variant Requires Shipping':'VRAI',
                'Variant Taxable':'VRAI',
                'Gift Card':'FAUX',
                'Variant Weight Unit':'g',
                'Status':'draft'
            }
            result.append(new_data)
    # 产品为varaince的情况
    else:
        tailles = df_data.loc[i,'Tailles']
        if not isinstance(tailles,float):
            list_taille = tailles.split(',')
            list_taille = [t.strip() for t in list_taille]
            l_taille_int = [t for t in list_taille if t.isdigit()]
            if l_taille_int:
                for l in l_taille_int:
                    new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                        #'Title':df_data.loc[i,'H1(Title)'] ,
                        #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                        #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                        #'Product Category':'',
                        #'Tags':df_data.loc[i,'Tags (tags_type)'],
                        #'Type':df_data.loc[i,'Tags (tags_type)'],
                        'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                        'Option1 Value':int(l),
                        #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                        #'Option2 Value':36,
                        #'Option3 Name':None,l
                        'Option3 Value':None,
                        'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + l,
                        'Variant Grams':df_data.loc[i,'Poids du produit'],
                        'Variant Inventory Tracker':'shopify',
                        'Variant Inventory Qty':3,
                        'Variant Inventory Policy':'deny',
                        'Variant Fulfillment Service':'manual',
                        'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                        'Variant Compare At Price':None,
                        'Variant Requires Shipping':'VRAI',
                        'Variant Taxable':'VRAI',
                       # 'Gift Card':'FAUX',
                        'Variant Weight Unit':'g',
                        #'Status':'draft'
                    }
                    result.append(new_data)
            else:
                for l in list_taille:
                    new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                        #'Title':df_data.loc[i,'H1(Title)'] ,
                        #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                        #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                        #'Product Category':'',
                        #'Tags':df_data.loc[i,'Tags (tags_type)'],
                        #'Type':df_data.loc[i,'Tags (tags_type)'],
                        'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                        'Option1 Value':l,
                        #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                        #'Option2 Value':36,
                        #'Option3 Name':None,l
                        'Option3 Value':None,
                        'Variant SKU':df_data.loc[i,'SKU variant']+ '-' + l,
                        'Variant Grams':df_data.loc[i,'Poids du produit'],
                        'Variant Inventory Tracker':'shopify',
                        'Variant Inventory Qty':3,
                        'Variant Inventory Policy':'deny',
                        'Variant Fulfillment Service':'manual',
                        'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                        'Variant Compare At Price':None,
                        'Variant Requires Shipping':'VRAI',
                        'Variant Taxable':'VRAI',
                      #  'Gift Card':'FAUX',
                        'Variant Weight Unit':'g',
                        #'Status':'draft'
                    }
                    result.append(new_data)
        # 没有taille选项
        else:
            new_data = {'Handle': df_data.loc[i,'URL(handle)'],
                    #'Title':df_data.loc[i,'H1(Title)'] ,
                    #'Body (HTML)':df_data.loc[i,'Description (Body)'],
                    #'Vendor':df_data.loc[i,'Fournisseur (vendor)'],
                    #'Product Category':'',
                    #'Tags':df_data.loc[i,'Tags (tags_type)'],
                    #'Type':df_data.loc[i,'Tags (tags_type)'],
                    'Option1 Name':df_data.loc[i,'Option 1 (option name)'],
                    #'Option1 Value':l,
                    #'Option2 Name':df_data.loc[i,'Option 2 (option name)'],
                    #'Option2 Value':36,
                    #'Option3 Name':None,l
                    'Option3 Value':None,
                    'Variant SKU':df_data.loc[i,'SKU variant'],
                    'Variant Grams':df_data.loc[i,'Poids du produit'],
                    'Variant Inventory Tracker':'shopify',
                    'Variant Inventory Qty':3,
                    'Variant Inventory Policy':'deny',
                    'Variant Fulfillment Service':'manual',
                    'Variant Price':df_data.loc[i,'Prix de vente TTC (Variant Price)'],
                    'Variant Compare At Price':None,
                    'Variant Requires Shipping':'VRAI',
                    'Variant Taxable':'VRAI',
                   # 'Gift Card':'FAUX',
                    'Variant Weight Unit':'g',
                    #'Status':'draft'
                }
            result.append(new_data)
    return result

if __name__ == '__main__': 
    if df_data.loc[0,'Option 1 (option name)'] == 'Couleur':
        result = data_avec_couleur_taille(0)
        for r in result:
            df_shopify = pd.concat([df_shopify ,pd.DataFrame([r])],axis=0)
    else:
        result =data_avec_taille(0)
        for r in result:
            df_shopify = pd.concat([df_shopify ,pd.DataFrame([r])],axis=0)
    for i in range(1, len(df_data)):
        
        if df_data.loc[i,'Option 1 (option name)'] == 'Couleur':
            result = data_avec_couleur_taille(i)
            for r in result:
                df_shopify = pd.concat([df_shopify ,pd.DataFrame([r])],axis=0)
        else:
            result =data_avec_taille(i)
            for r in result:
                df_shopify = pd.concat([df_shopify ,pd.DataFrame([r])],axis=0)
    writer = pd.ExcelWriter('new_shopify_3.xlsx')
    df_shopify.to_excel(writer,index = False)
    writer.save()

"""data_format = {'Handle': df_data['URL(handle)'],
            'Title':df_data['H1(Title)'] ,
            'Body (HTML)':df_data['Description (Body)'],
            'Vendor':df_data['Fournisseur (vendor)'],
            'Product Category':'',
            'Tags':df_data['Tags (tags_type)'],
            'Option1 Name':df_data['Option 1 (option name)'],
            'Option1 Value':df_data['Couleur'],
            'Option2 Name':df_data['Option 2 (option name)'],
            'Option2 Value':df_data['Tailles'],
            'Option3 Name':None,
            'Option3 Value':None,
            'Variant SKU':df_data['SKU variant'],
            'Variant Grams':df_data['Poids du produit'],
            'Variant Inventory Tracker':'shopify',
            'Variant Inventory Qty':3,
            'Variant Inventory Policy':'deny',
            'Variant Fulfillment Service':'manual',
            'Variant Price':df_data['Prix de vente TTC (Variant Price)'],
            'Variant Compare At Price':None,
            'Variant Requires Shipping':'VRAI',
            'Variant Taxable':'VRAI',
            'Gift Card':'FAUX',
            'Variant Weight Unit':'g',
            'Status':'draft'
            }"""