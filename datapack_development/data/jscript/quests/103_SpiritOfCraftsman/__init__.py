# Maked by Mr. Have fun! Version 0.2
print "importing quests: 103: Spirit Of Craftsman"
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

KAROYDS_LETTER_ID = 968
CECKTINONS_VOUCHER1_ID = 969
CECKTINONS_VOUCHER2_ID = 970
BONE_FRAGMENT1_ID = 1107
SOUL_CATCHER_ID = 971
PRESERVE_OIL_ID = 972
ZOMBIE_HEAD_ID = 973
STEELBENDERS_HEAD_ID = 974
BLOODSABER_ID = 975

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "1" :
        st.set("id","0")
        htmltext = "7307-05.htm"
        st.giveItems(KAROYDS_LETTER_ID,1)
        st.set("cond","1")
        st.setState(STARTED)
        st.playSound("ItemSound.quest_accept")
    return htmltext


 def onTalk (Self,npc,st):

   npcId = npc.getNpcId()
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.setState(STARTING)
     st.set("cond","0")
     st.set("onlyone","0")
     st.set("id","0")
   if npcId == 7307 and int(st.get("cond"))==0 and int(st.get("onlyone"))==0 :
        if int(st.get("cond"))<15 :
          if st.getPlayer().getRace().ordinal() != 2 :
            htmltext = "7307-00.htm"
          elif st.getPlayer().getLevel() >= 11 :
            htmltext = "7307-03.htm"
            return htmltext
          else:
            htmltext = "7307-02.htm"
            st.exitQuest(1)
        else:
          htmltext = "7307-02.htm"
          st.exitQuest(1)
   elif npcId == 7307 and int(st.get("cond"))==0 and int(st.get("onlyone"))==1 :
        htmltext = "<html><head><body>This quest have already been completed.</body></html>"
   elif npcId == 7307 and int(st.get("cond"))==1 and (st.getQuestItemsCount(KAROYDS_LETTER_ID)>=1 or st.getQuestItemsCount(CECKTINONS_VOUCHER1_ID)>=1 or st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID)>=1) :
        htmltext = "7307-06.htm"
   elif npcId == 7132 and int(st.get("cond"))==1 and st.getQuestItemsCount(KAROYDS_LETTER_ID)==1 and int(st.get("onlyone"))==0 :
        htmltext = "7132-01.htm"
        st.takeItems(KAROYDS_LETTER_ID,1)
        st.giveItems(CECKTINONS_VOUCHER1_ID,1)
   elif npcId == 7132 and int(st.get("cond"))==1 and (st.getQuestItemsCount(CECKTINONS_VOUCHER1_ID)>=1 or st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID)>=1) and int(st.get("onlyone"))==0 :
        htmltext = "7132-02.htm"
   elif npcId == 7144 and int(st.get("cond"))==1 and st.getQuestItemsCount(CECKTINONS_VOUCHER1_ID)>=1 and int(st.get("onlyone"))==0 :
        htmltext = "7144-01.htm"
        st.takeItems(CECKTINONS_VOUCHER1_ID,1)
        st.giveItems(CECKTINONS_VOUCHER2_ID,1)
   elif npcId == 7144 and int(st.get("cond"))==1 and st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID)>=1 and st.getQuestItemsCount(BONE_FRAGMENT1_ID)<10 and int(st.get("onlyone"))==0 :
        htmltext = "7144-02.htm"
   elif npcId == 7144 and int(st.get("cond"))==1 and st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID)==1 and st.getQuestItemsCount(BONE_FRAGMENT1_ID)>=10 and int(st.get("onlyone"))==0 :
          htmltext = "7144-03.htm"
          st.takeItems(CECKTINONS_VOUCHER2_ID,1)
          st.takeItems(BONE_FRAGMENT1_ID,10)
          st.giveItems(SOUL_CATCHER_ID,1)
   elif npcId == 7144 and int(st.get("cond"))==1 and st.getQuestItemsCount(SOUL_CATCHER_ID)==1 and int(st.get("onlyone"))==0 :
        htmltext = "7144-04.htm"
   elif npcId == 7132 and int(st.get("cond"))==1 and st.getQuestItemsCount(SOUL_CATCHER_ID)==1 and int(st.get("onlyone"))==0 :
          htmltext = "7132-03.htm"
          st.takeItems(SOUL_CATCHER_ID,1)
          st.giveItems(PRESERVE_OIL_ID,1)
   elif npcId == 7132 and int(st.get("cond"))==1 and st.getQuestItemsCount(PRESERVE_OIL_ID)==1 and st.getQuestItemsCount(ZOMBIE_HEAD_ID)==0 and st.getQuestItemsCount(STEELBENDERS_HEAD_ID)==0 and int(st.get("onlyone"))==0 :
        htmltext = "7132-04.htm"
   elif npcId == 7132 and int(st.get("cond"))==1 and st.getQuestItemsCount(ZOMBIE_HEAD_ID)==1 and int(st.get("onlyone"))==0 :
        htmltext = "7132-05.htm"
        st.takeItems(ZOMBIE_HEAD_ID,1)
        st.giveItems(STEELBENDERS_HEAD_ID,1)
   elif npcId == 7132 and int(st.get("cond"))==1 and st.getQuestItemsCount(STEELBENDERS_HEAD_ID)==1 and int(st.get("onlyone"))==0 :
        htmltext = "7132-06.htm"
   elif npcId == 7307 and int(st.get("cond"))==1 and st.getQuestItemsCount(STEELBENDERS_HEAD_ID)==1 and int(st.get("onlyone"))==0 :
        htmltext = "7307-07.htm"
        st.takeItems(STEELBENDERS_HEAD_ID,1)
        st.giveItems(BLOODSABER_ID,1)
        st.set("cond","0")
        st.setState(COMPLETED)
        st.playSound("ItemSound.quest_finish")
        st.set("onlyone","1")
   return htmltext

 def onKill (self,npc,st):

   npcId = npc.getNpcId()
   if npcId == 517 :
        st.set("id","0")
        if st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID) == 1 and st.getQuestItemsCount(BONE_FRAGMENT1_ID)<10 :
          if st.getRandom(10)<3 :
            st.giveItems(BONE_FRAGMENT1_ID,1)
            if st.getQuestItemsCount(BONE_FRAGMENT1_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
            else:
              st.playSound("ItemSound.quest_itemget")
   elif npcId == 518 :
        st.set("id","0")
        if st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID) == 1 and st.getQuestItemsCount(BONE_FRAGMENT1_ID)<10 :
          if st.getRandom(10)<3 :
            st.giveItems(BONE_FRAGMENT1_ID,1)
            if st.getQuestItemsCount(BONE_FRAGMENT1_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
            else:
              st.playSound("ItemSound.quest_itemget")
   elif npcId == 455 :
        st.set("id","0")
        if st.getQuestItemsCount(CECKTINONS_VOUCHER2_ID) == 1 and st.getQuestItemsCount(BONE_FRAGMENT1_ID)<10 :
          if st.getRandom(10)<3 :
            st.giveItems(BONE_FRAGMENT1_ID,1)
            if st.getQuestItemsCount(BONE_FRAGMENT1_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
            else:
              st.playSound("ItemSound.quest_itemget")
   elif npcId == 15 :
        st.set("id","0")
        if st.getQuestItemsCount(PRESERVE_OIL_ID) == 1 :
          if st.getRandom(10)<3 :
            st.giveItems(ZOMBIE_HEAD_ID,1)
            st.playSound("ItemSound.quest_middle")
            st.takeItems(PRESERVE_OIL_ID,1)
   elif npcId == 20 :
        st.set("id","0")
        if st.getQuestItemsCount(PRESERVE_OIL_ID) == 1 :
          if st.getRandom(10)<3 :
            st.giveItems(ZOMBIE_HEAD_ID,1)
            st.playSound("ItemSound.quest_middle")
            st.takeItems(PRESERVE_OIL_ID,1)
   return

QUEST       = Quest(103,"103_SpiritOfCraftsman","Spirit Of Craftsman")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(7307)

STARTING.addTalkId(7307)

STARTED.addTalkId(7132)
STARTED.addTalkId(7144)
STARTED.addTalkId(7307)

STARTED.addKillId(15)
STARTED.addKillId(20)
STARTED.addKillId(455)
STARTED.addKillId(517)
STARTED.addKillId(518)

STARTED.addQuestDrop(7307,KAROYDS_LETTER_ID,1)
STARTED.addQuestDrop(7132,CECKTINONS_VOUCHER1_ID,1)
STARTED.addQuestDrop(7144,CECKTINONS_VOUCHER2_ID,1)
STARTED.addQuestDrop(517,BONE_FRAGMENT1_ID,1)
STARTED.addQuestDrop(518,BONE_FRAGMENT1_ID,1)
STARTED.addQuestDrop(455,BONE_FRAGMENT1_ID,1)
STARTED.addQuestDrop(7144,SOUL_CATCHER_ID,1)
STARTED.addQuestDrop(7132,PRESERVE_OIL_ID,1)
STARTED.addQuestDrop(15,ZOMBIE_HEAD_ID,1)
STARTED.addQuestDrop(20,ZOMBIE_HEAD_ID,1)
STARTED.addQuestDrop(7132,STEELBENDERS_HEAD_ID,1)
