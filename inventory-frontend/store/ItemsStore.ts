import { defineStore } from 'pinia'

export const useItemsStore = defineStore('items', {
  state: () => ({
    //for search function filtering
    items: [],
    returnlist: [],
    newlist:[],
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
    //for filtering massive api
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
    return results
    },
    //filter api by category
    sort() {
      //choose api to filter by search 
      if (!this.search){
   this.items = this.returnlist;
      } else {
        this.items = this.newlist
      }
      //filter to different arrays
      this.coloring = this.items.filter((item) => item.category === "CM");
      this.craft = this.items.filter((item) => item.category === "CS");
      this.drawing = this.items.filter((item) => item.category === "DR");
      this.fabric = this.items.filter((item) => item.category === "FAB");
      this.firstaid = this.items.filter((item) => item.category === "FA");
      this.foam = this.items.filter((item) => item.category === "FM");
      this.glue = this.items.filter((item) => item.category === "GL");
      this.misc = this.items.filter((item) => item.category === "MISC");
      this.paint = this.items.filter((item) => item.category === "PT");
      this.paper = this.items.filter((item) => item.category === "PAP");
      this.print = this.items.filter((item) => item.category === "PRTM");
      this.sculpture = this.items.filter(
        (item) => item.category === "SC"
      );
      this.sewing = this.items.filter((item) => item.category === "SE");
      this.tape = this.items.filter((item) => item.category === "TP");
      this.tools = this.items.filter((item) => item.category === "TLS");
      this.wire = this.items.filter((item) => item.category === "WR");
      this.wood = this.items.filter((item) => item.category === "WD");
      //mass array of all filtered arrays
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
  }
  
})


