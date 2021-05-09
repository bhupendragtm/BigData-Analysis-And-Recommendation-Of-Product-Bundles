from ProductBundleRecommendation import settings
import json
import random

#first convert the json file from the path specified to python dict
path = settings.BASE_DIR / 'data.json'
with open(path) as f:
    product_bundles_lists = json.load(f)

#give avialable products randomly
def availableproducts():
    random_sample = random.sample(product_bundles_lists.keys(),20)
    data = []
    for item in random_sample:
        if(len(item)<70):
            data.append(item)
    return data
    
#lets find the top product bundles based on bigram frequency that was saved to data.json
def topproductbundledetails():
    topproductbundles = []
    for firstWord in product_bundles_lists:
        for secondWord in product_bundles_lists[firstWord]:
            if product_bundles_lists[firstWord][secondWord] > 20:           
                topproductDict = {
                    "firstproduct" : firstWord,
                    "secondproduct" : secondWord,
                    "frequency" : product_bundles_lists[firstWord][secondWord]
                }
                topproductbundles.append(topproductDict)
    
    return topproductbundles

def getPureData(prodName):
    
    '''sort the bigram frequencies in descending order, 
       then return merely the corresponding product names in the same order'''
    
    if prodName not in product_bundles_lists:
        return []
    sortedOringalList = sorted(product_bundles_lists[prodName].items(), key=lambda x: x[1], reverse=True)
    #     print(sortedOringalList)
    data = {}
    for tp in sortedOringalList:
        product = tp[0]
        number = tp[1]
        if number in data:
            productList = data[number]
            productList.append(product)
        else:
            productList = [product]
        data[number] = productList
    #     print(data)
    #     print("==> Get pure data name:")
    pureData = data.values()
    #     print(pureData)
    return list(pureData)

def pickRecommendProds(pureData, numberOfRecommend):
    
    '''Pick certain number of products from the sorted product names'''
    
    recommendProds = []
    for prods in pureData:
        if len(prods) <= numberOfRecommend:
            recommendProds += prods
            numberOfRecommend -= len(prods)
        else:
            recommendProds += random.sample(prods, numberOfRecommend)
            numberOfRecommend = 0

        if numberOfRecommend == 0:
            break
    
    return recommendProds

# recommend products bought together with 'name'
# name: the product to start with
def getRecommend(name, numberOfRecommend):
    
    '''Recommend certain number of products bought after the given input name'''
    recommendProducts = []
    productName = name
    index = 0

    while (numberOfRecommend):
    #         print("->Target: ", productName)
    #         print("->numberOfRecommend: ", numberOfRecommend)
    #         print("->Index: ", index)
        data = getPureData(productName)
    #     print("Pure data:", data)
        intermediate = pickRecommendProds(data, numberOfRecommend)
        recommendProducts += intermediate
    #         print("Recommend: ", recommendProducts)
    #         print("Recommend: ", recommendProducts)
        if len(intermediate) == 0 and index == len(recommendProducts):
            break
        numberOfRecommend -= len(intermediate)
        if numberOfRecommend > 0:
    #             print("Still left: ", numberOfRecommend)
            productName = recommendProducts[index]
            index += 1

    #         print("==================")

    return recommendProducts
