<template>
  <div class="popUpPanel vendorPanel">
    <canvas id="myChart" height="650"></canvas>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { Chart } from 'chart.js/auto';

const props = defineProps(["vendorName"])

let VendorItem = ref([])
let ItemCount = ref([])

const chartData = ref({
  labels: VendorItem.value,
  datasets: [
    {
      label: 'Total Stock Available',
      data: ItemCount.value,
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      backgroundColor: 'rgb(75, 1, 192)',
      tension: 0.1
    }
  ]
});

const chartOptions = ref({
  responsive: true,
  scales: {
    y: {
      beginAtZero: true,
    }, x: {
      ticks: {
        autoSkip: true,
        maxRotation: 80,
        minRotation: 80,
        fontSize: 16,
      },
      beforeUpdate(axis) {
        const labels = axis.chart.data.labels;
        for (let i = 0; i < labels.length; i++) {
          const lbl = labels[i];
          if (typeof lbl === 'string' && lbl.length > 10) {
            labels[i] = lbl.substring(0, 10) + "..."; // cutting
          }
        }
      }
    },
  },
  plugins: {
    legend: {
      labels: {
        font: {
          size: 14
        }
      }
    }
  }
});


const createChart = () => {
  const ctx = document.getElementById('myChart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'bar',
    data: chartData.value,
    options: chartOptions.value,
  });
};

onMounted(() => {
  fetchData();
});

async function fetchData() {
  try {
    const response = await fetch("http://127.0.0.1:8000/items/vendor/", {
      method: "GET",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow",
      referrerPolicy: "no-referrer",
    });

    const data = await response.json();

    const VendorName = props.vendorName
    data.forEach((vendor) => {
      if (VendorName === vendor.vendor_name) {
        vendor.itemsVendor.forEach((item) => {
          VendorItem.value.push(item.name)
          ItemCount.value.push(item.total)
        })
      }
    });

    createChart();
  } catch (error) {
    console.log("Error fetching data:", error);
  }
}

</script>

<style>
.popUpPanel {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

#myChart {
  position: relative;
  top: 5%;
  height: 100%;
}
</style>
