<template>
  <v-sheet width="300" class="mx-auto">
    <v-form @submit.prevent="open(fileLink)">
      <v-text-field
        v-model="fileLink"
        :rules="rules"
        label="File Link"
      ></v-text-field>
      <v-btn type="submit" block class="mt-2">Open</v-btn>
    </v-form>
  </v-sheet>
</template>

<script setup lang="ts">
import { ref } from "vue";
const emit = defineEmits(["open"])
const fileLink = ref();
const rules = [
  (value) => {
    if (value) return true;

    return "You must enter a first name.";
  },
];
const open = (link)=>{
  emit("open", link)
}
</script>
