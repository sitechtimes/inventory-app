import { defineStore } from "pinia";

export const useItemsStore = defineStore("items", {
  state: () => ({
    //for search function filtering
    items: [],
    returnlist: [],
    empty:false,
    search: false,
    //toggle extra info
    popup: { name: null },
    info: false,
    vendor: false,
    vendorHeader: false,
    categoryPop: false,
    categoryHeader: false,
    editform: false,
    //for resizing on toggling extra info
    main: [],
    textbox: [],
    name:[],
    quant:[],
    cat:[],
    //nav
    dismiss: true,
    catalog:true,
    monitor:false,
    vendors:false,
  }),

  getters: {},

  actions: {
    //fetch api
    async getItems(){
    const response = await fetch('http://127.0.0.1:8000/items/category')
    const results = await response.json()
    console.log(results)
    const newresults = results.sort((a,b) => (a.category_name > b.category_name) ? 1 : ((b.category_name > a.category_name) ? -1 : 0))
    this.returnlist = newresults

    this.items = newresults
    return newresults
    },
   
   
    //resize individual items when clicked for more information by adding/removing classes
    resizing() {
      if (this.info === true) {
        this.textbox.forEach((item) => {
          item.classList.add("info-name-avail");
        });
        this.name.forEach((item) => {
          item.classList.add("info-name");
        });
        this.quant.forEach((item) => {
          item.classList.add("info-quantity");
        });

        this.main.forEach((item) => {
          item.classList.remove("mainSize");
          item.classList.add("infoFull");
        });
        this.cat.forEach((item) => item.classList.add("info-cat"));
      } else {
        this.main.forEach((item) => {
          item.classList.add("mainSize");
          item.classList.remove("infoFull");
        });
        this.textbox.forEach((item) => {
          item.classList.remove("info-name-avail");
        });
        this.name.forEach((item) => {
          item.classList.remove("info-name");
        });
        this.quant.forEach((item) => {
          item.classList.remove("info-quantity");
        });
        this.cat.forEach((item) => item.classList.remove("info-cat"));
      }
    },
    //change classes for info pop up headers - inactive
    inactive(maintab, tabnumber, btn) {
      document.querySelector(maintab).classList.add("inactive");
      document.querySelector(tabnumber).classList.add("inactive");
      document.querySelector(btn).classList.add("inactivebtn");
    },
    //change classes for info pop up headers - active
    active(maintab, tabnumber, btn) {
      document.querySelector(maintab).classList.add("active");
      document.querySelector(maintab).classList.remove("inactive");
      document.querySelector(tabnumber).classList.remove("inactive");
      document.querySelector(btn).classList.remove("inactivebtn");
    },
    // clear search bar
    clearSearch() {
      this.$patch({
        search: false,
        info: false,
        items: this.returnlist,
      });

      document.getElementById("searchform").value = "";
    },
  }
  
})


