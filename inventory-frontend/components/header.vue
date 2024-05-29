<template>
  <div class="longrow">
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    />
    <div class="fixedleft">
      <div class="fromnav">
        <div class="navnavnavnav">
          <button class="open-menu-btn">
            <div
              v-if="store.dismiss === true"
              class="open-menu-icon-cont"
              @click="store.NavMenu"
            >
              <span
                class="material-symbols-outlined open-menu-icon"
                style="font-size: 30px"
              >
                menu
              </span>
            </div>
            <div
              v-if="store.dismiss === false"
              class="open-menu-icon-cont"
              @click="store.NavMenu"
            >
              <span
                class="material-symbols-outlined open-menu-icon"
                style="font-size: 30px"
              >
                close
              </span>
            </div>
          </button>
        </div>
      </div>

      <div class="heading sitename">Makerspace Inventory</div>
    </div>
    <li>
      <a class="nav-link" href="{% url'items_csv'%}">
          Item Csv
      </a>
    </li>
    <div class="searchbar">
      <Search />
    </div>
    <div class="buttonbar">
      <button class="addItem" @click="store.addItems">
        <span class="material-symbols-outlined add_box" style="font-size: 30px">
          add_box
        </span>
      </button>
      <button @click="viewNotifications" class="notif">
        <span class="material-symbols-outlined inbox" style="font-size: 30px">
          inbox
        </span>
        <div v-if="store.alerts > 0" class="smalltext alertNum"></div>
      </button>

      <div class="alerts-all" v-if="store.viewNotif">
        <Alerts />
      </div>
    </div>
  </div>
</template>

<script>
import Search from "./search.vue";
import Alerts from "./alerts.vue";
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Header",
  components: { Search, Alerts },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    viewNotifications() {
      let inbox = document.querySelector(".notif").classList;
      if (inbox.contains("spin")) {
        inbox.remove("spin");
        inbox.add("spin2");
      } else if (inbox.contains("spin2")) {
        inbox.add("spin");
        inbox.remove("spin2");
      } else {
        inbox.add("spin");
      }
      if (this.store.viewNotif === true) {
        this.store.$patch({
          viewNotif: false,
        });
      } else {
        this.store.$patch({
          viewNotif: true,
          info: false,
          vendor: false,
          vendorHeader: false,
          categoryPop: false,
          categoryHeader: false,
        });
        this.store.resizing();
      }
    },
  },
};
</script>

<style>
.addItem,
.notif {
  height: 4rem;
  width: 4rem;
  position: fixed;

  display: flex;
  align-items: center;
  justify-content: center;
}
.addItem {
  right: 7rem;
  border-radius: 2rem;
}
.addItem,
.add_box {
  transition: all 0.2s;
}
.add_box:hover {
  color: var(--darkblue);
}

.addItem:active {
  background-color: var(--lightblue);
}
.notif {
  right: 3rem;
}

.alerts-all,
.buttonbar {
  overflow-y: scroll;
}
.material-symbols-outlined {
  font-variation-settings: "FILL" 0, "wght" 400, "GRAD" 0, "opsz" 48;

  color: var(--darkestgray);
}
.alertNum {
  position: absolute;
  background-color: rgb(201, 37, 86);
  border-radius: 2rem;
  color: var(--whitebg);
  height: 1.25rem;
  width: 1.25rem;
  right: 0.5rem;
  top: 0.5rem;
  border: 2px solid var(--whitebg);
}
.navnavnavnav {
  width: 3rem;
  height: 3rem;
  margin: 0.5rem;
  display: flex;
  justify-content: center;
}
.fromnav {
  width: fit-content;

  position: fixed;
  left: 1.5rem;
}

.open-menu-btn {
  width: 100%;
  height: 100%;
  border: none;
  background-color: transparent;
}

.open-menu-icon {
  width: 100%;
  height: 100%;
  display: block;
}

.longrow {
  width: 100vw;
  height: 100%;
}
.longrow,
.searchbar,
.site-name,
.fixedleft,
.buttonbar {
  display: flex;
  flex-direction: row;

  align-items: center;
}
.fixedleft {
  width: 30%;
}
.searchbar {
  width: 55%;
  height: 100%;
}

.sitename {
  position: sticky;
  left: 8rem;
  margin-right: 0.5rem;
  overflow: hidden;
  width: 70%;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.buttonbar {
  width: 15%;
}

@media screen and (max-width: 1450px) {
  .searchform {
    margin-left: 0;
  }
}
@media screen and (max-width: 760px) {
  .sitename {
    visibility: collapse;
    width: 0;
  }
  .searchbar {
    width: 55%;
  }
  .fixedleft {
    width: 7rem;
  }
  .notif {
    right: 2rem;
  }
  .addItem {
    right: 6rem;
  }
}

/* animations  */
.selected {
  animation: slide-in 0.5s forwards;
}

.dismiss {
  animation: slide-out 0.5s forwards;
}

.stretch {
  animation: stretch 0.5s forwards;
}

.shrink {
  animation: shrink 0.5s forwards;
}

.spin {
  animation: spin 0.5s forwards;
}
.spin2 {
  animation: spin2 0.5s forwards;
}

@keyframes slide-in {
  0% {
    grid-template-columns: 7rem 1fr;
  }
  100% {
    grid-template-columns: 22rem 1fr;
  }
}

@keyframes slide-out {
  0% {
    grid-template-columns: 22rem 1fr;
  }
  100% {
    grid-template-columns: 7rem 1fr;
  }
}
@keyframes stretch {
  0% {
    width: 5rem;
  }
  100% {
    width: 20rem;
  }
}
@keyframes shrink {
  0% {
    width: 20rem;
  }
  100% {
    width: 5rem;
  }
}

@keyframes spin {
  0% {
    transform: rotate(0deg) scale(1);
  }
  50% {
    transform: rotate(180deg) scale(0);
  }
  100% {
    transform: rotate(360deg) scale(1);
  }
}

@keyframes spin2 {
  0% {
    transform: rotate(360deg) scale(1);
  }
  50% {
    transform: rotate(180deg) scale(0);
  }
  100% {
    transform: rotate(0deg) scale(1);
  }
}

@media screen and (max-width: 280px) {
  .selected {
    width: 100% !important;
  }
}
</style>
