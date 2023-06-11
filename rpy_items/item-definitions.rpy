##############################################################################
# InvItem class

init -2 python:
    class InvItem(store.object):
        def __init__(self, name, image, value, info, id, cost=None): #if you add any properties, list them up here, too!
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
define item_company_computer = (_("컴퓨터"), "company_computer", 1,
    _("작업 중이던 컴퓨터 이다"), "company_computer")
define item_company_hotsix = (_("음료"), "company_hotsix", 1,
    _("누군가가 마시던 음료이다"), "company_hotsix")
define item_company_cctv = (_("CCTV"), "company_cctv", 1,
    _("CCTV가 있다. 무언가 찍혔을까?"), "company_cctv")    
define item_company_knife = (_("커터칼"), "company_knife", 10,
    _("커터칼이 널브러져 있다"), "company_knife")
define item_company_nameteg = (_("사원증"), "company_nameteg", 1,
    _("사원증이다. 이걸 특별히 사용할 곳이 있을까?"), "company_nameteg")

define item_company_electricshocker = (_("전기충격기"), "company_electricshocker", 10,
    _("전기충격기이다. 이게 왜 여기에 있지?"), "company_electricshocker") 
define item_company_stapler = (_("스테이플러"), "company_stapler", 10,
    _("스테이플러다. 증거가 될 수도 있겠군."), "company_stapler") 
define item_company_port = (_("커피포트"), "company_port", 10,
    _("커피포트이다."), "company_port") 
define item_company_wire = (_("전선"), "company_wire", 10,
    _("전선이다. 이게 왜 여기에 있지? 범행에 쓰였을지도 모르겠군."), "company_wire")
define item_company_coffee = (_("커피"), "company_coffee", 1,
    _("흔히 볼 수 있는 커피다."), "company_coffee")
define item_company_view = (_("창문"), "company_view", 1,
    _("이 창문에서는 이러한 풍경이 보이네. 혹시 단서가 될까?"), "company_view") 
define item_company_thirsty = (_("말라죽은 화분"), "company_thirsty", 1,
        _("오랫동안 관리되지 않았나본데, 무슨 일이 있었을까?"), "company_thirsty")

#병원 아이템
define item_hospital_drug = (_("약물"), "hospital_drug", 10,#
    _("수상한 약물이다"), "hospital_drug")
define item_hospital_knife = (_("메스"), "hospital_knife", 10, #
    _("날카로운 메스다. 수술실에 있어야 할 것이 왜 여기에 있지?"), "hospital_knife")
define item_hospital_syringe = (_("주사기"), "hospital_syringe", 10, #
    _("병원에서 많이 쓰는 주사기이다"), "hospital_syringe")
define item_hospital_memo = (_("메모"), "hospital_memo", 10, #
    _("이건 대체 무슨 내용일까?"), "hospital_memo")
define item_hospital_file = (_("서류파일"), "hospital_file", 10,#
    _("이 파일도 단서가 될 수 있을거 같군."), "hospital_file")

define item_hospital_cutter = (_("커터칼"), "hospital_cutter", 10, #
    _("이 커터칼은 왜 여기에 들어있지?"), "hospital_cutter")
define item_hospital_broken = (_("깨진 화분"), "hospital_broken", 10, #
    _("이 화분은 어쩌다가 깨지게 되었을까?"), "hospital_broken") 
define item_hospital_pillow = (_("베개"), "hospital_pillow", 10, #
    _("베개군. 베개가 터진 점이 수상해."), "hospital_pillow")
define item_hospital_drink = (_("음료수 병"), "hospital_drink", 10, #
    _("흔히 볼 수 있는 음료수 병이다. 별 다른 점은 없을까?"), "hospital_drink")
define item_hospital_curtain = (_("커튼"), "hospital_curtain", 10, #
    _("이 커튼은 왜 늘어져 있지? 혹시 질식사?"), "hospital_curtain")


define item_hospital_pass = (_("출입증"), "hospital_pass", 1, #
    _("출입증이군. 이걸 통해 출입 시간을 알 수 있겠어."), "hospital_pass")
define item_hospital_book1 = (_("꽂힌 책"), "hospital_book1", 1, #
    _("이 책도 단서가 될 수 있을까?"), "hospital_book1") 
define item_hospital_stethoscope = (_("청진기"), "hospital_stethoscope", 1, #
    _("여기에 올려져 있는 청진기는 범행에 쓰였을까?"), "hospital_stethoscope")
define item_hospital_bed = (_("침대"), "hospital_bed", 1,
    _("침대가 젖어있네. 왜 젖어있지?"), "hospital_bed")

define item_hospital_window = (_("창문"), "hospital_window", 1, #
    _("이 창문에서는 이러한 풍경이 보이네. 혹시 단서가 될까?"), "hospital_window")
define item_hospital_book2 = (_("책"), "hospital_book2", 1, #
    _("책이다. 단서가 될 수도 있겠군."), "hospital_book2")


#별장 아이템
define item_villa_gun = (_("엽총"), "villa_gun", 10,
    _("취미가 사냥인 사람이 있었나?"), "villa_gun")
define item_villa_knife = (_("식칼"), "villa_knife", 10,
    _("주방에 있어야 할 식칼이 왜 방에서 나오지?"), "villa_knife")
define item_villa_rope = (_("밧줄"), "villa_rope", 1,
    _("적당한 길이의 밧줄이다"), "villa_rope")
define item_villa_saw = (_("톱"), "villa_saw", 10,
    _("날카로운 톱이다. 무엇이든 자를 수 있을 것 같다"), "villa_saws")
define item_villa_pillow = (_("베개"), "villa_pillow", 1,
    _("베개군. 베개가 터진 점이 수상해."), "villa_pillow")

define item_villa_glass = (_("유리조각"), "villa_glass", 10,
    _("유리조각이다. 무슨일이 있었던 거지?"), "villa_glass")
define item_villa_syringe = (_("주사기"), "villa_syringe", 10,
    _("병원에서 많이 쓰는 주사기이다"), "villa_syringe")
define item_villa_deco = (_("장식물"), "villa_deco", 10,
    _("장식물이 무겁고 단단해보인다."), "villa_deco")
define item_villa_picture1 = (_("풍경화"), "villa_picture1", 1,
    _("고급스러워보이는 풍경화이다. 이건 뭐지?"), "villa_picture1")
define item_villa_memo = (_("메모"), "villa_memo", 1,
    _("이건 대체 무슨 내용일까?"), "villa_memo")
define item_villa_coffee = (_("커피"), "villa_coffee", 1,
    _("흔히 볼 수 있는 커피다."), "villa_coffee")
define item_villa_picture2 = (_("비싼 그림"), "villa_picture2", 1,
    _("비싸보이는 그림이다. 단서가 될 수 있을까?"), "villa_picture2")
define item_villa_sight = (_("풍경"), "villa_sight", 1,
    _("밖은 이러한 풍경이군. 혹시 단서가 될까?"), "villa_sight")
define item_villa_monitor = (_("모니터"), "villa_monitor", 1,
    _("모니터이다. 여기 안에 단서가 있을지도 몰라."), "villa_monitor")
define item_villa_mirror = (_("거울"), "villa_mirror", 1,
    _("커다란 거울이다. "), "villa_monitor")


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
    item_company_electricshocker, 
    item_company_stapler,
    item_company_port, 
    item_company_wire,
    item_company_coffee,
    item_company_view, 
    item_company_thirsty,
    #병원 아이템
    item_hospital_drug,
    item_hospital_knife,
    item_hospital_syringe,
    item_hospital_memo,
    item_hospital_file,
    item_hospital_cutter,
    item_hospital_broken, 
    item_hospital_pillow, 
    item_hospital_drink,
    item_hospital_curtain,
    item_hospital_pass,
    item_hospital_book1,
    item_hospital_stethoscope, 
    item_hospital_bed,
    item_hospital_window,
    item_hospital_book2,

    #별장 아이템
    item_villa_gun,
    item_villa_knife,
    item_villa_rope, 
    item_villa_saw, 
    item_villa_pillow,
    item_villa_glass,
    item_villa_syringe, 
    item_villa_deco,
    item_villa_picture1, 
    item_villa_memo,
    item_villa_coffee, 
    item_villa_picture2,
    item_villa_sight,
    item_villa_monitor,
    item_villa_mirror
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
