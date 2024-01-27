<script type="ts">
    import image from "../../assets/WorkInProgress.jpg"
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
<link href="https://fonts.googleapis.com/css2?family=Abril+Fatface&family=Cairo&family=Montserrat&family=Philosopher&family=Roboto+Slab&display=swap" rel="stylesheet">
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .centered {
            text-align: center;
        }

        .work-in-progress {
            font-family: 'Cairo', sans-serif;
            color:black;
            font-size: 60px;
            margin-bottom: 20px;
            margin-top: -265px;
            margin-left: 0px;
        }

        .animated-image {
            animation: bounce 1s infinite;
            margin-top: 135px;
            margin-left: 81px;
        }

        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% {
                transform: translateY(0);
            }
            40% {
                transform: translateY(-20px);
            }
            60% {
                transform: translateY(-10px);
            }
        }
    </style>
<title>Work In Progress</title>
<body>
    <div class="centered">
        <p class="work-in-progress">Under Construction</p>
        <img src={image} alt="Work in progress" class="animated-image">
    </div>
</body>
