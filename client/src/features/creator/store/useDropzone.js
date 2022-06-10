import { defineStore } from "pinia";

const useDropzone = defineStore({
  id: "cardCreator",
  state: () => ({ dropzoneBlocks: [] }), // { id: block1, placedItem: { type: 'text' | 'photo', width: , height, base64?: photo, text: string } }
  actions: {
    setItem(blockId, placedItem) {
      if (placedItem.previousBlockId) {
        this.dropzoneBlocks = this.dropzoneBlocks.map((block) =>
          block.id === placedItem.previousBlockId ? ({ ...block, placedItem: undefined }) : block
        );
      }
      if (!this.dropzoneBlocks.find((block) => block.id === blockId)) {
        this.dropzoneBlocks = [
          ...this.dropzoneBlocks,
          { id: blockId, placedItem },
        ];
      } else {
        this.dropzoneBlocks = this.dropzoneBlocks.map((block) =>
          block.id === blockId ? ({ ...block, placedItem }) : block
        );
      }
    },
    updateItem(blockId, item) {
      this.dropzoneBlocks = this.dropzoneBlocks.map((block) =>
          block.id === blockId ? ({ ...block, placedItem: { ...block.placedItem, ...item } }) : block
        );
    },
    getItem(blockId) {
      return this.dropzoneBlocks.find(block => block.id === blockId)?.placedItem;
    },
    onSave() {
      //TODO
    },
  },
});

export default useDropzone;