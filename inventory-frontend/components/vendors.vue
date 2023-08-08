<template>
  <div class="bigdiv bigdivV">
    <div id="mainItems">
      <div class="itemHeader subheading">Vendors</div>
    </div>
    <div class="infoPop">
      <div class="tabPop heading">
        <div>Vendor</div>
      </div>
      <div class="extraInfoPanel">
        <VendorInfo :vendorName="ShopDOE" />
      </div>
    </div>
  </div>
</template>

<script>
import VendorInfo from "./vendorInfo.vue";

export default {
  name: "Vendors",
  components: {
    VendorInfo,
  },
};
</script>

<style>
.chart-cont {
  height: 70rem;
  width: 70rem;
}
</style>
