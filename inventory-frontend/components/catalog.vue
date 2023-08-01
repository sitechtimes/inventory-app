<template>
  <div class="bigdiv">
    <div id="mainItems">
      <div id="itemHeader" class="subheading">Items</div>
      <div
        class="errorsearch subheading"
        v-if="store.search === true && store.newlist.length < 1"
      >
        No Items
      </div>
      <div id="itemHolderAll" ref="allItems">
        <div class="categoryHolder">
          <ItemPerCat
            v-for="(each, index) in store.returnlist"
            :key="each.id"
            :list="each.itemsCategory"
            :name="nameType(index)"
            :min="minimum(each)"
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
      />
    </div>
  </div>
</template>

<script>
import ItemPerCat from "./itemPerCat.vue";
import Info from "./info.vue";
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Catalog",
  components: { ItemPerCat, Info },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    minimum(list) {
      if (list.length >= 1) {
        return true;
      } else {
        return false;
      }
    },
    nameType(number) {
      if (number === 0) {
        return "Paint";
      } else if (number === 1) {
        return "Sculpture";
      } else if (number === 2) {
        return "Print Making";
      } else if (number === 3) {
        return "Craft Supplies";
      } else if (number === 4) {
        return "Fabric";
      } else if (number === 5) {
        return "Coloring Materials";
      } else if (number === 6) {
        return "Tools";
      } else if (number === 7) {
        return "Wood";
      } else if (number === 8) {
        return "Tape";
      } else if (number === 9) {
        return "Glue";
      } else if (number === 10) {
        return "First Aid";
      } else if (number === 11) {
        return "Foam";
      } else if (number === 12) {
        return "Miscellaneous";
      } else if (number === 13) {
        return "Sewing";
      } else if (number === 14) {
        return "Paper";
      } else if (number === 15) {
        return "Wire";
      } else if (number === 16) {
        return "Drawing";
      } else {
        return "Error";
      }
    },
  },
  mounted() {
    this.store.getItems();
  },
};
</script>

<style>
.bigdiv {
  display: flex;
  flex-direction: row;
  overflow-y: hidden;
  background-color: var(--lightgray);
  min-width: 100%;
}
#mainItems {
  display: flex;
  flex-direction: column;
  width: 100%;
}
#itemHeader {
  min-height: 5.5rem;
  border-bottom: var(--border);
  background-color: var(--whitebg);
  position: sticky;
  top: 0;
  z-index: 500;
  display: flex;
  align-items: center;
  padding-left: 2rem;
}
#itemHolderAll {
  grid-column: 2 / 3;
  grid-row: 3 / 4;

  justify-content: center;
  overflow-y: scroll;
  height: 100%;
  width: 100%;
  flex: 1 1 0%;
}

.infoDesc {
  height: 100%;
  width: 70%;
  min-width: 50rem;
  position: sticky;
  top: 0;
  overflow: hidden;
  flex: 1 1 0%;
  border-left: var(--border);
  z-index: 2000;
}
.errorsearch {
  text-align: center;
  min-width: 100%;
  color: var(--darkestgray);
  margin-top: 5rem;
}

@media screen and (min-width: 1600px) {
  .infoDesc {
    min-width: 80rem;
  }
}
@media screen and (max-width: 760px) {
  .infoDesc {
    width: auto;
    align-self: flex-start;
    justify-self: flex-start;
    position: fixed;
    margin-top: 5.5rem;
    margin-left: 7rem;
    left: 0;
    right: 0;
    border: none;
  }
}
</style>
