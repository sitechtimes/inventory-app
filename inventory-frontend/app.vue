<template>
  <div class="app">
    <div id="search" class="heading">search</div>
    <div id="navHolder">nav</div>
    <div id="itemHeader" class="subheading">items</div>
    <div id="itemHolderAll">
      <div class="category">
        <ItemPerCat
          v-for="(each, index) in categories"
          :key="index"
          :category="each"
          :name="nameType(index)"
        ></ItemPerCat>
      </div>
    </div>
  </div>
</template>

<style>
.app {
  height: 100%;
  width: 100%;
  display: grid;
  grid-template-columns: 7rem 1fr;
  grid-template-rows: 5.5rem 5.5rem 1fr;
  position: absolute;
  top: 0;
  left: 0;
  overflow: hidden;
}
#search {
  grid-column: 1 / 3;
  width: 100%;
  height: 100%;
  border-bottom: solid 1px var(--darkgray);
}
#navHolder {
  grid-row: 2 / 4;
  grid-column: 1 / 2;
  border-right: solid 1px var(--darkgray);
}
#itemHeader {
  grid-row: 2/3;
  grid-column: 2/3;
  border-bottom: solid 1px var(--darkgray);
}
#itemHolderAll {
  grid-column: 2 / 3;
  grid-row: 3 / 4;
  background-color: var(--lightgray);
  justify-content: center;
  overflow-y: scroll;
  height: 100%;
  width: 100%;
  flex-direction: column;
}
</style>

<script>
import ItemPerCat from "./components/itemPerCat.vue";
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "app",
  components: { ItemPerCat },
  data() {
    return {
      all: useItemsStore(),
      categories: [],
      coloring: [],
      craft: [],
      drawing: [],
      fabric: [],
      firstaid: [],
      foam: [],
      glue: [],
      misc: [],
      paint: [],
      paper: [],
      print: [],
      sculpture: [],
      sewing: [],
      tape: [],
      tools: [],
      wire: [],
      wood: [],
    };
  },
  methods: {
    sort() {
      this.coloring = this.all.items.filter((item) => item.category === "CM");
      this.craft = this.all.items.filter((item) => item.category === "CS");
      this.drawing = this.all.items.filter((item) => item.category === "DR");
      this.fabric = this.all.items.filter((item) => item.category === "FAB");
      this.firstaid = this.all.items.filter((item) => item.category === "FA");
      this.foam = this.all.items.filter((item) => item.category === "FM");
      this.glue = this.all.items.filter((item) => item.category === "GL");
      this.misc = this.all.items.filter((item) => item.category === "MISC");
      this.paint = this.all.items.filter((item) => item.category === "PT");
      this.paper = this.all.items.filter((item) => item.category === "PAP");
      this.print = this.all.items.filter((item) => item.category === "PRTM");
      this.sculpture = this.all.items.filter((item) => item.category === "SC");
      this.sewing = this.all.items.filter((item) => item.category === "SE");
      this.tape = this.all.items.filter((item) => item.category === "TP");
      this.tools = this.all.items.filter((item) => item.category === "TLS");
      this.wire = this.all.items.filter((item) => item.category === "WR");
      this.wood = this.all.items.filter((item) => item.category === "WD");

      console.log(this.categories);

      this.categories = [
        this.coloring,
        this.craft,
        this.drawing,
        this.fabric,
        this.firstaid,
        this.foam,
        this.glue,
        this.misc,
        this.paint,
        this.paper,
        this.print,
        this.sculpture,
        this.sewing,
        this.tape,
        this.tools,
        this.wire,
        this.wood,
      ];
    },
    nameType(number) {
      if (number === 0) {
        return "Coloring Materials";
      } else if (number === 1) {
        return "Craft Supplies";
      } else if (number === 2) {
        return "Drawing";
      } else if (number === 3) {
        return "Fabric";
      } else if (number === 4) {
        return "First Aid";
      } else if (number === 5) {
        return "Foam";
      } else if (number === 6) {
        return "Glue";
      } else if (number === 7) {
        return "Miscellaneous";
      } else if (number === 8) {
        return "Paint";
      } else if (number === 9) {
        return "Paper";
      } else if (number === 10) {
        return "Print Making";
      } else if (number === 11) {
        return "Sculpture";
      } else if (number === 12) {
        return "Sewing";
      } else if (number === 13) {
        return "Tape";
      } else if (number === 14) {
        return "Tools";
      } else if (number === 15) {
        return "Wire";
      } else if (number === 16) {
        return "Wood";
      } else {
        return "Error";
      }
    },
  },
  async mounted() {
    await this.all.getItems();
    this.sort();
  },
};
</script>
