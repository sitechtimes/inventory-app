<template>
  <div class="longrow">
    <div class="fixedleft">
      <div class="fromnav">
        <div class="navnavnavnav"></div>
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
export default {
  name: "Header",
  components: { Search },
};
</script>

<style>
.navnavnavnav {
  width: 4rem;
  height: 4rem;
  border: 1px solid black;
  margin: 1rem;
}
.fromnav {
  width: fit-content;

  position: fixed;
  left: 1rem;
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
  width: 35%;
}
.searchbar {
  width: 50%;
  height: 100%;
}

.sitename {
  position: sticky;
  left: 8rem;

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
  height: 4rem;
  width: 4rem;
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
    visibility: hidden;
  }
  .searchbar {
    width: 70%;
  }
  .fixedleft {
    width: 9rem;
  }
}
</style>
