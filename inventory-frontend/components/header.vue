<template>
  <div class="longrow">
    <div class="fixedleft">
      <div class="fromnav">
        <div class="navnavnavnav">
          <button class="open-menu-btn">
            <div
              v-if="store.dismiss === true"
              class="open-menu-icon-cont"
              @click="store.NavMenu"
            >
              <font-awesome-icon
                :icon="['fas', 'bars']"
                class="open-menu-icon"
              />
            </div>
            <div
              v-if="store.dismiss === false"
              class="open-menu-icon-cont"
              @click="store.NavMenu"
            >
              <font-awesome-icon
                :icon="['fas', 'xmark']"
                style="color: #000000"
                class="open-menu-icon"
              />
            </div>
          </button>
        </div>
      </div>

      <div class="heading sitename">Makerspace Inventory</div>
    </div>

    <div class="searchbar">
      <Search />
    </div>
    <div class="buttonbar">
      <div class="notif"></div>
    </div>
  </div>
</template>

<script>
import Search from "./search.vue";
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "Header",
  components: { Search },
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {},
};
</script>

<style>
.navnavnavnav {
  width: 2rem;
  height: 2rem;
  margin: 1rem;
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
.notif {
  border: 1px solid black;
  height: 3rem;
  width: 3rem;
  position: fixed;
  right: 3rem;
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
    width: 70%;
  }
  .fixedleft {
    width: 7rem;
  }
  .notif {
    right: 2rem;
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
</style>
