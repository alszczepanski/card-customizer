const fileAsBase64 = (file, onSuccess) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      onSuccess(reader.result);
    };
    reader.onerror = (error) => {
      console.log("Error: ", error);
    };
  };

export default fileAsBase64;