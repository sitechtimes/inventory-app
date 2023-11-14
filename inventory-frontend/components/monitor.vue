<template>
  <div class="bigdiv bigdivM">
    <div class="monitorCol">
      <div id="mainItems" class="monitorSticky">
        <div class="itemHeader subheading">Monitor</div>
        <div class="subheadorg">
          <div class="itemSub subname heading">Name</div>
          <div class="itemSub totalstock heading">Total Stock Available</div>
        </div>
      </div>

      <div class="itemHolderAll monitorHolder">
        <div class="categoryHolder search" v-if="store.search">
          <ItemPerCat
            v-for="each in store.items"
            :key="each[0]"
            :list="each[1]"
            :name="each[0]"
          ></ItemPerCat>
        </div>
        <div class="categoryHolder" v-else>
          <ItemPerCat
            v-for="each in store.items"
            :key="each.id"
            :list="each.itemsCategory"
            :name="each.category_name"
          ></ItemPerCat>
        </div>
      </div>
    </div>

    <div class="infoDesc" v-if="store.info" ref="infoHolder">
      <Info
        :img_link="store.popup.image"
        :name="store.popup.name"
        :category="store.popup.category"
        :quantity="store.popup.quantity"
        :link="store.popup.link"
        :vendor="store.popup.vendor"
        :date="store.popup.updated"
        :backroom_quantity="store.popup.backroom"
        :makerspace_quantity="store.popup.makerspace"
        :min_amount="store.popup.min_amount"
      />
    </div>
  </div>
</template>

<script>
import ItemPerCat from "./itemPerCat.vue";
import Info from "./info.vue";
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "Monitor",
  components: { ItemPerCat, Info },
  data() {
    return {
      store: useItemsStore(),
    };
  },
};
</script>

<style>
.bigdivM {
  display: flex;
  justify-content: left;
  flex-direction: column;
}
.monitorHolder {
  margin-right: 0;
}
.monitorCol {
  width: 100%;
}
.subheadorg {
  width: 100%;
  background-color: var(--whitebg);
  border-bottom: var(--border);
  display: flex;
  flex-direction: row;
}
.itemSub {
  padding: 1rem 2rem;
}
.subname {
  width: 60%;
  max-width: 70rem;
}
.totalstock {
  border-left: var(--border);
  max-width: 25rem;
  width: 20%;
  overflow: hidden;

  white-space: nowrap;
  text-overflow: ellipsis;
}
.monitorSticky {
  position: sticky;
  top: 0;
}
</style>
