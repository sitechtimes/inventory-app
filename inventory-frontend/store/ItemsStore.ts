import { defineStore } from "pinia";
import { showNotification } from "assets/globalVar";
export const useItemsStore = defineStore("items", {

  state: () => ({
    //for search function filtering
    logs: [],
    items: [],
    returnlist: [],
    pulledinfo: {},
    empty: false,
    search: false,
    //toggle extra info
    id: 0,
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
    name: [],
    quant: [],
    cat: [],
    //nav
    dismiss: true,
    catalog: true,
    monitor: false,
    vendors: false,
    //notifying minimum
    alerts: 0,
    alerted_items: [],
    viewNotif: false,
  }),
  getters: {},
  
  actions: {
    //fetch api

    async getLogs(itemname){
      try {
        console.log("LOGS")
        const config = useRuntimeConfig()
        const response = await fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/log/`);
        const results = await response.json();
        console.log(results);
        this.logs = results.filter(el => el.name === itemname);
        this.logs.sort((a, b) => a.pub_date.localeCompare(b.pub_date));
        this.logs = this.logs.reverse()
        console.log(this.logs)
      } catch (error) {
        // TypeError: Failed to fetch ubgiiuhguygivuyig
        console.log('There was an error', error);
      }

    },

    async getItems() {

      const config = useRuntimeConfig()
      const response = await fetch(`${config.public.protocol}://${config.public.baseurl}:${config.public.port}/items/category/`);
      const results = await response.json();
      console.log(results);
      const newresults = results.sort((a, b) =>

        a.category_name > b.category_name
          ? 1
          : b.category_name > a.category_name
          ? -1
          : 0
      );
      this.returnlist = newresults;
      this.items = newresults;

     

      this.resizing()
    },   
    //resize individual items when clicked for more information by adding/removing classes
    resizing() {
      
      if (this.info === true || this.editform === true) {
        document.querySelectorAll('.itemMain').forEach((item) => {
          item.classList.remove("mainSize");
          item.classList.add("infoFull");
        });
        this.cat.forEach((item) => item.classList.add("info-cat"));
        console.log('LOL')
      } else {
        document.querySelectorAll('.itemMain').forEach((item) => {
          item.classList.add("mainSize");
          item.classList.remove("infoFull");
        });
        console.log('RESIZE')
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
    //nav menu reshape
    NavMenu() {
      this.viewNotif = false;
      this.editform = false;
      const appDOM = document.querySelector(".app");
      const menubtn = document.querySelectorAll(".menu-btn");
      if (appDOM.classList.contains("selected")) {
        appDOM.classList.remove("selected");
        appDOM.classList.add("dismiss");
        menubtn.forEach((btn) => {
          btn.classList.remove("stretch");
          btn.classList.add("shrink");
        });

        this.dismiss = true;
        console.log("dismiss");
      } else if (appDOM.classList.contains("dismiss")) {
        appDOM.classList.remove("dismiss");
        this.dismiss = false;
        this.info = false;
        appDOM.classList.add("selected");
        menubtn.forEach((btn) => {
          btn.classList.remove("shrink");
          btn.classList.add("stretch");
        });
        console.log("selected");
      } else if (
        !appDOM.classList.contains("dismiss") ||
        !appDOM.classList.contains("selected")
      ) {
        appDOM.classList.add("selected");
        console.log("selected");
        menubtn.forEach((btn) => {
          btn.classList.add("stretch");
        });
      }
    },
    //counting alerts
    countAlerts() {
      this.returnlist.forEach((list) => {
        console.log(list);
        list.itemsCategory.forEach((item) => {
          if (item.alert === true) {
            this.alerts++;
            this.alerted_items.push({
              name: item.name,
              quantity: item.total,
              name_id: item.name_id,
            });
          }
        });
      });
      console.log(this.alerts);
    },
    //add item form
    addItems() {
      console.log('pp')
      if (this.editform === true) {
        this.editform = false;
      } else {
        this.editform = true;
        (this.viewNotif = false),
          (this.info = false),
          (this.vendor = false),
          (this.vendorHeader = false),
          (this.categoryPop = false),
          (this.categoryHeader = false);
      }
      this.resizing();
    },
  },
});
