-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-12-2023 a las 17:08:30
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `base`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `archivo`
--

CREATE TABLE `archivo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `pdf` text NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_materia` int(11) NOT NULL,
  `id_tipo` int(11) NOT NULL,
  `fecha` varchar(30) NOT NULL,
  `revisado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `archivo`
--

INSERT INTO `archivo` (`id`, `nombre`, `pdf`, `id_usuario`, `id_materia`, `id_tipo`, `fecha`, `revisado`) VALUES
(13, 'test 1234', '34ef5c10-8e86-4de5-b3dc-9f6f7f12b783.pdf', 60, 2, 6, '2023-11-23 18:39:32.106753', 'No Revisado'),
(14, 'Guia programación Web', '8fe4988f-4e6f-47ee-b06e-166b55324c66.pdf', 1, 36, 10, '2023-11-24 15:51:13.318366', 'No Revisado'),
(21, 'Apuntes ', '69594f11-b034-4eae-a6c1-fb95392fa050.pdf', 62, 40, 11, '2023-12-02 00:52:40.595350', 'No Revisado'),
(25, 'resumen informatica conce', '44f7c75b-05fe-4684-ade2-2c75f05690db.pdf', 1, 2, 5, '2023-12-05 12:20:08.786260', 'Revisado'),
(26, 'ultima prueba', '3574ed9c-9d74-4695-b4d2-b0c2dff5f46a.pdf', 1, 36, 15, '2023-12-05 13:04:45.198944', 'No Revisado'),
(27, 'apuntes fuerza elastica', '7dd5c4e2-c4e9-4632-b89e-44adc6d2e164.pdf', 3, 38, 11, '2023-12-06 12:35:00.569551', 'No Revisado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios`
--

CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_archivo` int(11) NOT NULL,
  `textocomentario` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comentarios`
--

INSERT INTO `comentarios` (`id`, `id_usuario`, `id_archivo`, `textocomentario`) VALUES
(82, 1, 21, 'MUY BUENOS APUNTES, TE FELICITO!'),
(83, 1, 25, 'holaaa');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `control_like`
--

CREATE TABLE `control_like` (
  `id` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_archivo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `control_like`
--

INSERT INTO `control_like` (`id`, `id_usuario`, `id_archivo`) VALUES
(14, 55, 15),
(15, 55, 16),
(72, 5, 11),
(74, 5, 14),
(87, 1, 12),
(93, 1, 19),
(97, 1, 3),
(98, 1, 18),
(110, 1, 14),
(115, 5, 18),
(116, 1, 13),
(117, 1, 20),
(118, 1, 11),
(119, 62, 13),
(120, 62, 14),
(121, 62, 17),
(122, 62, 21),
(123, 1, 22),
(125, 1, 25),
(126, 1, 21),
(127, 1, 26),
(128, 3, 27),
(129, 3, 25),
(130, 3, 21),
(131, 3, 14),
(132, 3, 13),
(133, 3, 26);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `favoritos`
--

CREATE TABLE `favoritos` (
  `id` int(11) NOT NULL,
  `id_archivo` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `favoritos`
--

INSERT INTO `favoritos` (`id`, `id_archivo`, `id_usuario`) VALUES
(19, 12, 1),
(20, 16, 1),
(23, 16, 5),
(54, 14, 62),
(56, 22, 1),
(57, 21, 1),
(59, 25, 1),
(60, 26, 1),
(61, 27, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `materias`
--

CREATE TABLE `materias` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `materias`
--

INSERT INTO `materias` (`id`, `nombre`) VALUES
(29, 'Álgebra y Geometría'),
(42, 'Cálculo Avanzado'),
(30, 'Filosofía y Antropología'),
(38, 'Física II'),
(2, 'Informatica general'),
(40, 'Matematica '),
(43, 'Programación Orientada a Objetos'),
(36, 'Programación Web'),
(6, 'Quimica general'),
(37, 'Seminario I');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipos`
--

CREATE TABLE `tipos` (
  `id` int(11) NOT NULL,
  `nombre` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipos`
--

INSERT INTO `tipos` (`id`, `nombre`) VALUES
(5, 'Resumen'),
(6, 'Parcial'),
(10, 'Otros...'),
(11, 'Apuntes'),
(12, 'Esquema'),
(13, 'Recuperatorio'),
(14, 'Mapa Conceptual'),
(15, 'Final');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(15) NOT NULL,
  `apellido` varchar(15) NOT NULL,
  `nomusuario` varchar(15) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contrasena` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `nomusuario`, `email`, `contrasena`) VALUES
(1, 'Fede', 'Rosenfeld', 'ADMIN', 'federosenfeld.nqn@gmail.com', 'fedefede'),
(2, '', '', '', '', ''),
(3, 'test', 'test12', 'test123', 'test123@gmail.com', 'testtest'),
(4, 'thola', 'test12', 'holaa', 'test1234567@gmail.com', 'test1234'),
(5, 'marti', 'rosenfeld', 'marosen', 'asd@asd.com', 'asdasdasdasd'),
(48, 'nacho', 'holaA', 'nacho123', 'nacho@gmail.com', 'nachonacho'),
(50, 'luis', 'Ivanoff', 'luis123', 'luis@gmail.com', 'luis1234'),
(52, 'tato', 'mantel', 'blabla', 'tato@gmail.com', 'tato1234'),
(54, 'tato', 'mantel', 'blablaa', 'tatoo@gmail.com', 'tato1234'),
(55, 'asd', 'asd', 'fedefedefede', 'fedefede@gmail.com', 'asdasdasd'),
(57, 'jorge', 'alvarez', 'jorguito', 'jorgue@egmail.com', 'jorgue1234'),
(58, 'ssss', 'ssss', 'blablaaaaa', 'bla@gmailll.com', 'asdasdasd'),
(59, 'entrega', 'final', 'entregafinal', 'entregafinal@gmail.com', 'entregafinal'),
(60, 'Juan', 'Rosenfeld', 'Juan1234', 'juan@gmail.com', 'juan1234'),
(62, 'Carina', 'Alvarez', 'alvarezc', 'abcdabcd10@gmail.com', 'caricari'),
(63, 'raul', 'perez', 'raul123', 'raul@gmail.com', 'raulraul'),
(64, 'test', 'final', 'testfinal', 'test@gmail.com', 'test1234');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `archivo`
--
ALTER TABLE `archivo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_archivo_materias` (`id_materia`),
  ADD KEY `fk_archivo_tipos` (`id_tipo`);

--
-- Indices de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_comentarios_usuario` (`id_usuario`),
  ADD KEY `fk_comentarios_archivo` (`id_archivo`);

--
-- Indices de la tabla `control_like`
--
ALTER TABLE `control_like`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_like_usuario` (`id_usuario`),
  ADD KEY `fk_like_archivo` (`id_archivo`);

--
-- Indices de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_favoritos_usuario` (`id_usuario`),
  ADD KEY `fk_favoritos_archivo` (`id_archivo`);

--
-- Indices de la tabla `materias`
--
ALTER TABLE `materias`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `tipos`
--
ALTER TABLE `tipos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`) USING HASH;

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nomusuario` (`nomusuario`),
  ADD UNIQUE KEY `unique` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `archivo`
--
ALTER TABLE `archivo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=84;

--
-- AUTO_INCREMENT de la tabla `control_like`
--
ALTER TABLE `control_like`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;

--
-- AUTO_INCREMENT de la tabla `favoritos`
--
ALTER TABLE `favoritos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT de la tabla `materias`
--
ALTER TABLE `materias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT de la tabla `tipos`
--
ALTER TABLE `tipos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `archivo`
--
ALTER TABLE `archivo`
  ADD CONSTRAINT `fk_archivo_materias` FOREIGN KEY (`id_materia`) REFERENCES `materias` (`id`),
  ADD CONSTRAINT `fk_archivo_tipos` FOREIGN KEY (`id_tipo`) REFERENCES `tipos` (`id`),
  ADD CONSTRAINT `fk_archivo_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD CONSTRAINT `fk_comentarios_archivo` FOREIGN KEY (`id_archivo`) REFERENCES `archivo` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `fk_comentarios_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `control_like`
--
ALTER TABLE `control_like`
  ADD CONSTRAINT `fk_like_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
