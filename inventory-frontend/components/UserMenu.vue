<template>
  <div>
    <div class="menu">
      <div class="menu-container">
        <button class="menu-btn exitbtn shrink" @click="catalog">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'boxes-stacked']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Items</div>
          <div class="popup-tag text" v-if="store.dismiss">Items</div>
        </button>

        <button class="menu-btn exitbtn shrink" @click="monitor">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'hand-holding-hand']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Monitor</div>
          <div class="popup-tag text" v-if="store.dismiss">Monitor</div>
        </button>

        <button class="menu-btn exitbtn shrink" @click="vendors">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'circle-exclamation']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Vendors</div>
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
      this.store.$patch({ catalog: true, monitor: false, vendors: false });
    },
    monitor() {
      this.store.$patch({ catalog: false, monitor: true, vendors: false });
    },
    vendors() {
      this.store.$patch({ catalog: false, monitor: false, vendors: true });
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
  z-index: 1000;
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
  color: #c7d6d5;
  width: 2.5rem;
  height: 2.5rem;
  margin: 0 1rem;
}
</style>
