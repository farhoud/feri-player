<template>
  <div class="subtitle">
    <v-chip  size="x-large" variant="flat" color="primary" v-if="show" class="ma-2" closable @click:close="clear()">
      {{ translation }}
    </v-chip>

    <p  :draggable="false" ref="text" @mouseup="handleMouseUp">
      {{ correctedText }}
    </p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";

const props = defineProps({
  text: String,
  playing: Boolean,
});

const emit = defineEmits(["select", "clear"]);

const correctedText = ref(props.text);
const translation = ref();
const show = ref(false);

const clear = () => {
  const selection = window.getSelection();
  if (selection) {
    selection.removeAllRanges();
  }
  show.value = false;
  emit("clear");
};

const handleMouseUp = () => {
  const selection = window.getSelection();
  if (selection) {
    emit("select");
    const selectedText = selection.toString().trim();
    translate(selectedText);
    // if (selectedText.length > 0) {
    //   const textNode = selection.anchorNode;

    //   if (textNode) {
    //     const textContent = textNode.textContent || "";
    //     const selStart = Math.min(
    //       selection.anchorOffset,
    //       selection.focusOffset
    //     );
    //     const selEnd = Math.max(selection.anchorOffset, selection.focusOffset);
    //     console.log(textContent);
    //     console.log(selection.anchorOffset);
    //     const wordStart = textContent.lastIndexOf(" ", selStart) + 1;
    //     console.log(selection.focusOffset);
    //     console.log(selection);
    //     let wordEnd = textContent.indexOf(" ", selEnd);
    //     wordEnd = wordEnd !== -1 ? wordEnd : textContent.length - 1;
    //     const correctedWord = textContent.slice(wordStart, wordEnd);
    //     selection.removeAllRanges();
    //     const range = document.createRange();
    //     range.setStart(textNode, wordStart);
    //     range.setEnd(textNode, wordEnd);
    //     selection.addRange(range);
    //     translate(correctedWord);
    //     console.log(correctedWord);
    //   }
    // }
  }
};
const translate = async (text) => {
  try {
    const response = await fetch(`http://127.0.0.1:8000/translate/${text}`);
    const data = await response.json();

    // Assuming the API returns a JSON object with a 'translation' property
    translation.value = data.translation;
    show.value = true;
  } catch (error) {
    console.error("Error fetching translation:", error);
  }
};

watch(
  () => props.text,
  () => {
    correctedText.value = props.text;
  }
);
watch(
  () => props.playing,
  (newVal, preVal) => {
    if (newVal === true && preVal === false) {
      clear();
    }
  }
);

onMounted(() => {
  // Additional setup logic if needed
});
</script>

<style scoped>
/* Add your styles here */
.subtitle {
  font-size: 36px;
  font-weight: bold;
  color: rgb(237, 215, 14);
  text-align: center;
  box-shadow: 2px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}
</style>
