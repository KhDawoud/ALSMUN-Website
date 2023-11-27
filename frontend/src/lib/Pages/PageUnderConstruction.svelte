<script type="ts">
    import image from "../../assets/WorkInProgress.jpg"
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
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
            font-family: 'Comic Sans', sans-serif; /* Change the font family to Open Sans */
            font-size: 20px;
            margin-bottom: 20px;
        }

        .animated-image {
            animation: bounce 1s infinite;
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
        <p class="work-in-progress">Work In Progress</p>
        <img src={image} alt="Work in progress" class="animated-image">
    </div>
</body>
