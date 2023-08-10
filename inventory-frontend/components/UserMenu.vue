<template>
  <div>
    <link
      rel="stylesheet"
      href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
    />
    <div class="menu">
      <div class="menu-container">
        <button
          class="menu-btn exitbtn shrink catalogbtn activepage"
          @click="catalog"
        >
          <div class="icon-holder">
            <span
              class="material-symbols-outlined mobile-icon shelves activetag"
            >
              shelves
            </span>
          </div>
          <div class="icon-tag heading cat-tag activetag">Items</div>
          <div class="popup-tag text" v-if="store.dismiss">Items</div>
        </button>

        <button class="menu-btn exitbtn shrink monitorbtn" @click="monitor">
          <div class="icon-holder">
            <span class="material-symbols-outlined mobile-icon monitoring">
              monitoring
            </span>
          </div>
          <div class="icon-tag heading mon-tag">Monitor</div>
          <div class="popup-tag text" v-if="store.dismiss">Monitor</div>
        </button>

        <button class="menu-btn exitbtn shrink vendorsbtn" @click="vendors">
          <div class="icon-holder">
            <span class="material-symbols-outlined mobile-icon shipping">
              local_shipping
            </span>
          </div>
          <div class="icon-tag heading ven-tag">Vendors</div>
          <div class="popup-tag text" v-if="store.dismiss">Vendors</div>
        </button>
      </div>
    </div>

    <!-- <div class="return-box" @click="NavMenu">
    </div> -->
  </div>
</template>

<script>
import { useItemsStore } from "~/store/ItemsStore";
export default {
  name: "UserMenu",
  props: {},
  components: {},
  data() {
    return {
      store: useItemsStore(),
    };
  },
  methods: {
    catalog() {
      this.store.clearSearch();
      this.store.$patch({
        catalog: true,
        monitor: false,
        vendors: false,
        viewNotif: false,
      });
      document.querySelector(".catalogbtn").classList.add("activepage");
      document.querySelector(".monitorbtn").classList.remove("activepage");
      document.querySelector(".vendorsbtn").classList.remove("activepage");
      document.querySelector(".cat-tag").classList.add("activetag");
      document.querySelector(".mon-tag").classList.remove("activetag");
      document.querySelector(".ven-tag").classList.remove("activetag");
      document.querySelector(".shelves").classList.add("activetag");
      document.querySelector(".monitoring").classList.remove("activetag");
      document.querySelector(".shipping").classList.remove("activetag");
    },
    monitor() {
      this.store.clearSearch();
      this.store.$patch({
        catalog: false,
        monitor: true,
        vendors: false,
        viewNotif: false,
      });
      document.querySelector(".catalogbtn").classList.remove("activepage");

      document.querySelector(".monitorbtn").classList.add("activepage");
      document.querySelector(".vendorsbtn").classList.remove("activepage");
      document.querySelector(".cat-tag").classList.remove("activetag");
      document.querySelector(".mon-tag").classList.add("activetag");
      document.querySelector(".ven-tag").classList.remove("activetag");
      document.querySelector(".shelves").classList.remove("activetag");
      document.querySelector(".monitoring").classList.add("activetag");
      document.querySelector(".shipping").classList.remove("activetag");
    },
    vendors() {
      this.store.clearSearch();
      this.store.$patch({
        catalog: false,
        monitor: false,
        vendors: true,
        viewNotif: false,
      });
      document.querySelector(".catalogbtn").classList.remove("activepage");

      document.querySelector(".monitorbtn").classList.remove("activepage");
      document.querySelector(".vendorsbtn").classList.add("activepage");
      document.querySelector(".cat-tag").classList.remove("activetag");
      document.querySelector(".mon-tag").classList.remove("activetag");
      document.querySelector(".ven-tag").classList.add("activetag");
      document.querySelector(".shelves").classList.remove("activetag");
      document.querySelector(".shipping").classList.add("activetag");
      document.querySelector(".monitoring").classList.remove("activetag");
    },
  },
};
</script>

<style scoped>
.nav-cont {
  height: 100vh;
  width: 18rem;

  display: flex;
  flex-flow: row;
}

.menu-container {
  width: 100%;
  display: flex;
  flex-flow: column nowrap;
  align-items: left;
  margin: 0 1rem;
  margin-top: 1rem;
}

.menu-btn {
  padding: 0.3rem;
  border: none;
  margin: 0.2rem 0;
  text-decoration: none;
  display: grid;
  grid-template-columns: 8rem 1fr;
  transition: background-color 0.2s linear;
}
.icon-holder {
  grid-column: 1 / 2;
}
.icon-tag {
  color: var(--black);
  grid-column: 2 / 3;
  text-align: left;
}
.icon-holder,
.icon-tag {
  display: flex;
  align-items: center;
  height: 100%;
}
.popup-tag {
  position: absolute;
  left: 5.5rem;
  margin-top: 1rem;
  z-index: 10000;
  width: fit-content;
  clip-path: polygon(
    10% 0,
    100% 0%,
    100% 100%,
    10% 100%,
    10% 60%,
    0 50%,
    10% 40%
  );
  background-color: var(--tpdarkestgray);
  color: var(--whitebg);
  padding: 0.5rem 0.75rem 0.5rem 1.5rem;
  text-align: left;
  opacity: 0;
  transform: scale(0);
  transition: all 0.15s;
}

.menu-btn:hover > .popup-tag {
  transform: scale(1);
  opacity: 1;
}
.catalog-icon,
.borrowed-icon,
.needed-icon {
  color: #c7d6d5;
  width: 2rem;
  height: 2rem;
}

.mobile-icon {
  display: grid;
  color: var(--darkestgray);
  width: 2.5rem;
  height: 2.5rem;
  margin: 0 1rem;
}
.activepage {
  background-color: var(--lightblue);
}
.activepage:hover {
  background-color: var(--lightblue);
}
.activetag {
  color: var(--darkblue);
}
</style>
