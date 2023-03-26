const download = async() => {
    const response = await fetch('CSV file location in backend');
    const blob = await Response.blob();
    const url = URL.createObjectURL(blob);
    const data = document.createElement('data');
    data.href = url;
    data.download = 'data.csv';
    document.body.appendChild(data);
    data.click();
    document.body.removeChild(data);
};