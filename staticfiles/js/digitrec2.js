
let model;

async function loadModel() {
    console.log("model loading..");
    model = undefined;
    model = tf.loadLayersModel("/models/model.json");
    console.log("model loaded..");
}

loadModel();

function processCanvas(image) {
    let tensor = tf.browser.fromPixels(image)
        .resizeNearestNeighbor([28, 28])
        .mean(2)
        .expandDims(2)
        .expandDims()
        .toFloat();
    console.log(tensor.shape);
    return tensor.div(255.0);
}

$("#predict-button").click(async function () {
        var imageData = canvas.toDataURL();
        let tensor = processCanvas(canvas);
        console.log("tensor loaded...");
        let predictions = model.predict(tensor).data();
        let results = Array.from(predictions);
        console.log(results);
        console.log("testing");
});