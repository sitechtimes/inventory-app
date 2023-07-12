<template>
  <div class="app">
    <div id="search" class="heading">search</div>
    <div id="navHolder">nav</div>
    <div id="itemHeader" class="subheading">items</div>
    <div id="itemHolderAll">
      <div class="subheading catHead">Coloring</div>
      <div class="itemHolder">
        <Item
          v-for="result in coloring"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Craft Supplies</div>
      <div class="itemHolder">
        <Item
          v-for="result in craft"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Drawing</div>
      <div class="itemHolder">
        <Item
          v-for="result in drawing"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Fabric</div>
      <div class="itemHolder">
        <Item
          v-for="result in fabric"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">First Aid</div>
      <div class="first">
        <Item
          v-for="result in craft"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Foam</div>
      <div class="itemHolder">
        <Item
          v-for="result in foam"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Glue</div>
      <div class="itemHolder">
        <Item
          v-for="result in glue"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :description="result.purchase_link"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Miscellaneous</div>
      <div class="itemHolder">
        <Item
          v-for="result in misc"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Paint</div>
      <div class="itemHolder">
        <Item
          v-for="result in paint"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Paper</div>
      <div class="itemHolder">
        <Item
          v-for="result in paper"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Printmaking</div>
      <div class="itemHolder">
        <Item
          v-for="result in print"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Sculpture</div>
      <div class="itemHolder">
        <Item
          v-for="result in sculpture"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Sewing</div>
      <div class="itemHolder">
        <Item
          v-for="result in sewing"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Tape</div>
      <div class="itemHolder">
        <Item
          v-for="result in tape"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Tools</div>
      <div class="itemHolder">
        <Item
          v-for="result in tools"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Wire</div>
      <div class="itemHolder">
        <Item
          v-for="result in wire"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
      </div>

      <div class="subheading catHead">Wood</div>
      <div class="itemHolder">
        <Item
          v-for="result in wood"
          :key="result.id"
          :name="result.name"
          :quantity="result.quantity"
          :image="result.image"
          :available="true"
          :updated="result.last_purchased"
        />
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
.itemHolder {
  display: flex;
  height: fit-content;
  width: 100%;
  flex-direction: row;
  flex-wrap: wrap;
}
</style>

<script>
import Item from "./components/item.vue";
import { useItemsStore } from "~/store/ItemsStore";

export default {
  name: "app",
  components: { Item },
  data() {
    return {
      all: useItemsStore(),
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
      this.tape = this.all.items.filter((item) => item.category === "TLS");
      this.tools = this.all.items.filter((item) => item.category === "TP");
      this.wire = this.all.items.filter((item) => item.category === "WR");
      this.wood = this.all.items.filter((item) => item.category === "WD");
    },
  },
  mounted() {
    this.all.getItems();
    setTimeout(this.sort, 50);
  },
};
</script>
