<template>
  <div>
    <div class="menu">
      <div class="menu-container">
        <button class="menu-btn exitbtn shrink">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'boxes-stacked']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Items</div>
        </button>
        <button class="menu-btn exitbtn shrink">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'hand-holding-hand']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Monitor</div>
        </button>
        <button class="menu-btn exitbtn shrink">
          <div class="icon-holder">
            <font-awesome-icon
              :icon="['fas', 'circle-exclamation']"
              class="mobile-icon"
            />
          </div>
          <div class="icon-tag heading">Vendors</div>
        </button>
      </div>
    </div>

    <!-- <div class="return-box" @click="NavMenu">
    </div> -->
  </div>
</template>

<script>
export default {
  name: "UserMenu",
  props: {},
  components: {},
  data() {
    return {};
  },
  methods: {},
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
h2,
h3 {
  color: black;
  padding-left: 0.5rem;
  font-size: 0.6rem;
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
