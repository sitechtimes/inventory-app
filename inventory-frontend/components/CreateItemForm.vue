<template>
  <div class="form-container">
    <form @submit.prevent="submitForm">
      <div class="input-container">
        <label for="name">Name of the Item</label>
        <input id="name" type="text" placeholder="Enter the Name of the Item" required />
      </div>
      <div class="input-container">
        <label>Quantity</label>
        <div class="quantity-inputs">
          <input id="quantity-makerspace" type="number" placeholder="Maker Space Quantity" required />
          <input id="quantity-backroom" type="number" placeholder="Back Room Quantity" required />
        </div>
      </div>
      <div class="input-container">
        <label for="location">Location of the Item</label>
        <input id="location" type="text" placeholder="Enter the location of the Item" required />
      </div>
      <div class="input-container">
        <label for="Vendor">Vendor</label>
        <select id="Vendor" required>
          <option value="">Choose a Vendor</option>
          <option value="DOE">ShopDOE</option>
          <option value="AMZ">Amazon</option>
          <option value="BLICK">Blick</option>
          <option value="HD">Home Depot</option>
        </select>
      </div>
      <div class="input-container">
        <label for="Category">Category</label>
        <select id="Category" required>
          <option value="">Choose a Category</option>
          <option value="TLS">Tools</option>
          <option value="PT">Paint</option>
          <!-- Add other options here -->
        </select>
      </div>

      <!-- image pre view container  -->
      <div class="upload-container relative flex items-center justify-between w-full">
        <div
          class="drop-area w-full rounded-md border-2 border-dotted border-gray-200 transition-all hover:border-blue-600/30 text-center"
          @dragover.prevent="handleDragOver" @dragleave="handleDragLeave" @drop.prevent="handleDrop">
          <label for="file-input" class="block w-full h-full text-gray-500 p-4 text-sm cursor-pointer">
            {{ dropAreaText }}
          </label>
          <input name="file" type="file" id="file-input" accept="image/*" class="hidden" @change="handleFileChange" />
          <!-- Image upload input -->
          <div class="preview-container" :class="{ hidden: !showPreview }">
            <div class="preview-image w-36 h-36 bg-cover bg-center rounded-md cursor-pointer"
              :style="{ backgroundImage: previewImage }" @click="handleImageClick"></div>
            <span class="file-name my-4 text-sm font-medium" v-if="fileName">{{ fileName }}</span>
            <p class="close-button cursor-pointer transition-all mb-4 rounded-md px-3 py-1 border text-xs text-red-500 border-red-500 hover:bg-red-500 hover:text-white"
              @click="handleClose">
              Delete
            </p>
          </div>
        </div>

        <!-- Bigger Image Preview Modal -->
        <div class="modal" v-if="showModal" @click="closeModal">
          <div class="modal-content">
            <img :src="previewImageModal" alt="Bigger Preview" @click="closeModal" />
          </div>
        </div>
      </div>
      <button class="submit-button" @click="submitForm">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";

// State variables
const dropAreaText = ref("Drop your image here or click to browse");
const showPreview = ref(false);
const showModal = ref(false);
const previewImage = ref("");
const previewImageModal = ref("");
const fileName = ref("");

// Functions
function handleDragOver(event) {
  event.preventDefault();
  dropAreaText.value = "Drop your image here";
}

function handleDragLeave() {
  dropAreaText.value = "Drop your image here or click to browse";
}

function handleDrop(event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  showPreview.value = true;
  if (file) {
    showPreview.value = true;
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        previewImage.value = `url(${reader.result})`;
        previewImageModal.value = reader.result;
        fileName.value = file.name;
      };
    }
  }
}

function handleFileChange(event) {
  const file = event.target.files[0];
  showPreview.value = true;
  if (file) {
    showPreview.value = true;
    if (file.type.startsWith("image/")) {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        previewImage.value = `url(${reader.result})`;
        previewImageModal.value = reader.result;
        fileName.value = file.name;
      };
    }
  }
}

function handleClose() {
  showPreview.value = false;
  fileName.value = "";
  previewImage.value = "";
}

function handleImageClick() {
  showModal.value = true;
}

function closeModal() {
  showModal.value = false;
}
</script>

<style scoped>
.submit-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.submit-button:hover {
  background-color: #45a049;
}

.submit-button:active {
  background-color: #3e8e41;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  max-width: 90%;
  max-height: 90%;
}

.modal img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.upload-container {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.drop-area {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  border-radius: 0.375rem;
  border: 2px dotted #cbd5e0;
  transition: border-color 0.2s ease;
}

.drop-area:hover {
  border-color: #4299e1;
}

.drop-area label {
  color: #4a5568;
  width: 100%;
  height: 100%;
  padding: 1rem;
  font-size: 2rem;
  font-weight: 500;
  cursor: pointer;
  text-align: center;
}

/* Hidden file input styles */
.hidden {
  display: none !important;

}

/* Preview container styles */
.preview-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.preview-image {
  width: 16rem;
  height: 16rem;
  background-color: #e2e8f0;
  background-size: cover;
  background-position: center;
  border-radius: 0.375rem;
}

.file-name {
  margin-top: 1rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.close-button {
  cursor: pointer;
  transition: all 0.2s ease;
  margin-bottom: 2rem;
  padding: 0.25rem 0.75rem;
  border: 1px solid #e53e3e;
  font-size: 1rem;
  color: #e53e3e;
  border-radius: 0.25rem;
}

.close-button:hover {
  background-color: #e53e3e;
  color: #fff;
}

.form-container {
  max-width: 650px;
  margin: 0 auto;
  padding: 2rem;
  background-color: #f5f5f5;
  border-radius: 0.5rem;
}

form {
  display: grid;
  gap: 1.5rem;
}

.input-container {
  display: grid;
  gap: 0.5rem;
}

label {
  font-weight: bold;
}

input,
select {
  padding: 0.8rem;
  font-size: 1.6rem;
  border: 1px solid #ccc;
  border-radius: 0.3rem;
}

.quantity-inputs {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.submit-container {
  display: flex;
  justify-content: center;
}
</style>
