CREATE TABLE `entries` (
  `id` int(0) NOT NULL COMMENT 'id',
  `title` tinytext NOT NULL COMMENT '博客标题',
  `content` text NOT NULL COMMENT '博客内容',
  `posted_on` datetime(0) NOT NULL COMMENT '博客发布时间',
  PRIMARY KEY (`id`)
);