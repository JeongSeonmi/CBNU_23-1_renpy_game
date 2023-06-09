##############################################################################
# InvItem class

init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=[]): #if you add any properties, list them up here, too!
            self.name = name #item name (as seen by the player)
            self.image = image #item art
            self.value = int(value) #market price
            self.info = info #item description
            self.id = id #string to be used as a codename
        #!! IMPORTANT !! don't change the order of anything above this line!
            ## INSERT REQUIRED PROPERTIES HERE ##
            self.cost = cost #list of ingredients, only necessary for craftable items
            ## INSERT OPTIONAL PROPERTIES HERE ##

    ## INVITEM FUNCTIONS

        # add item to the list of seen items
        def see(self):
            if self.id not in seen_items:
                seen_items.append(self.id)

        # add crafting recipe to the list of seen recipes
        def see_recipe(self):
            if self.id not in seen_recipes:
                seen_recipes.append(self.id)

        # see the item and add it to your inventory
        def pickup(self, amount=1):
            self.see()
            global gold
            while amount>0:
                inv.append(self.id)
                gold += self.value
                amount -= 1            

        # discard the item from your inventory
        def toss(self, amount):
            while amount>0:
                inv.remove(self.id)
                amount -= 1

        # exchange gold for an item
        def buy(self, amount):
            global gold

            self.see()

            gold -= self.value*amount
            while amount>0:
                inv.append(self.id)
                amount -=1

        # exchange an item for gold
        def sell(self, amount):
            global gold

            gold += int(self.value*amount/2)
            self.toss(amount)

        # craft an item
        def make(self, amount):

            self.see()

            while amount>0:
                for i in self.cost:
                    inv.remove(i)
                inv.append(self.id)
                made_recipes.append(self.id)
                amount -=1

        #for shop screen--checks that you can afford to buy 1 of any item
        def check_price(self):
            if self.value <= gold:
                return True
            return False

##############################################################################
# more functions! (not part of InvItem)

    # turns the item tuple into the item object
    def set_item(self):

        for i in itemlist:
            if self==i[4]: #checks the id--this is why you can't change the order!!
                return i

    #inventory sorting
    def sortbyname(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.name

    def sortbyprice(i):
        thisitem = InvItem(*set_item(i))
        return thisitem.value

    # for crafting-screens.rpy--checks that you are able to craft at least 1 of the item
    def check_ingredients(craftitem):

        check = 0
        for i in craftitem.cost:
            if inv.count(i) > 0:
                check += 1

        if check == len(craftitem.cost):
            return True

        return False

    # used to check if you have battle items in battle-screens.rpy--but you can make other lists to check for too!
    def check_inv_for(itemtype):
        for i in itemtype:
            if inv.count(i) > 0:
                return True

##############################################################################
# ITEM DEFINITIONS

# INGREDIENTS
define item_cookie = (_("CoCoCookie"), "item_cookie", 8,
    _("테스트로 만드는 쿠키입니다!"), "item_cookie")
define item_post = (_("post"), "item_post", 8,
    _("용의자들의 역할이 적힌 메모"), "item_post")
define item_painting = (_("painting"), "item_painting", 8,
    _("값비싸 보이는 그림이다"), "item_painting")
#회사 아이템
define item_company_computer = (_("컴퓨터"), "company_computer", 8,
    _("작업 중이던 컴퓨터 이다"), "company_computer")
define item_company_hotsix = (_("음료"), "company_hotsix", 8,
    _("누군가가 마시던 음료이다"), "company_hotsix")
define item_company_cctv = (_("CCTV"), "company_cctv", 8,
    _("CCTV가 있다. 무언가 찍혔을까?"), "company_cctv")    
define item_company_knife = (_("커터칼"), "company_knife", 8,
    _("커터칼이 널브러져 있다"), "company_knife")
define item_company_nameteg = (_("사원증"), "company_nameteg", 8,
    _("사원증이다. 이걸 특별히 사용할 곳이 있을까?"), "company_nameteg")    


#병원 아이템
define item_hospital_drug = (_("약물"), "hospital_drug", 8,
    _("수상한 약물이다"), "hospital_drug")
define item_hospital_knife = (_("메스"), "hospital_knife", 8,
    _("날카로운 메스다. 수술실에 있어야 할 것이 왜 여기에 있지?"), "hospital_knife")
define item_hospital_sytinge = (_("주사기"), "hospital_syringe", 8,
    _("병원에서 많이 쓰는 주사기이다"), "hospital_syringe")

#별장 아이템
define item_villa_gun = (_("엽총"), "villa_gun", 8,
    _("취미가 사냥인 사람이 있었나?"), "villa_gun")
define item_villa_knife = (_("식칼"), "villa_knife", 8,
    _("주방에 있어야 할 식칼이 왜 방에서 나오지?"), "villa_knife")
define item_villa_rope = (_("밧줄"), "villa_rope", 8,
    _("적당한 길이의 밧줄이다"), "villa_rope")
define item_villa_saw = (_("톱"), "villa_saw", 8,
    _("날카로운 톱이다. 무엇이든 자를 수 있을 것 같다"), "villa_saws")



##############################################################################
# ITEM LISTS

# ALL ITEMS (every single one!!)
define itemlist = [
    
    item_cookie,
    item_post,
    item_painting,
    #회사 아이템
    item_company_computer,
    item_company_hotsix,
    item_company_cctv,    
    item_company_knife,
    item_company_nameteg,


    #병원 아이템
    item_hospital_drug,
    item_hospital_knife,
    item_hospital_sytinge,
    
    #별장 아이템
    item_villa_gun,
    item_villa_knife,
    item_villa_rope,
    item_villa_saw

    ]

# all items that can be crafted
define allrecipes = [
    "item_sugar",
    "item_sucker"
    ]

# all items that can be used in battle
define battle_items = [
    "item_sucker"
    ]

## INSERT NEW RECIPE LISTS HERE ##

# for recipes screen
define recipelists = [ allrecipes, battle_items ]
define recipelist_names = [ _("All"), _("Battle") ]
