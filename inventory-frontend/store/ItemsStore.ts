import { defineStore } from 'pinia'

export const useItemsStore = defineStore('items', {
  state: () => ({
    //for search function filtering
    items: [],
    returnlist: [],
    empty:false,
    search: false,
    //toggle extra info
    popup: {name:null},
    info: false,
    vendor:false,
    vendorHeader: false,
    categoryPop: false,
    categoryHeader: false,
    editform:false,
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

  getters: {

  },

  actions: {
    //fetch api
    async getItems(){
    const response = await fetch('http://127.0.0.1:8000/items/category')
    const results = await response.json()
    console.log(results)
    this.returnlist = results
    this.items = results
    return results
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
    //Headers
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
  }
  
})


